import math
from flask import Flask, Response, render_template, request
import pandas as pd

app = Flask(__name__)

CSV_PATH = "leads.csv"
ITEMS_PER_PAGE = 20
EXPECTED_COLUMNS = [
    "id",
    "company_name",
    "category",
    "country",
    "city",
    "address",
    "phone",
    "website",
    "rating",
]


def load_leads():
    df = pd.read_csv(CSV_PATH)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required CSV columns: {missing}")
    return df


def contains_value(series, value):
    return series.astype(str).str.contains(value, case=False, na=False, regex=False)


def apply_filters(df, city="", country="", category="", search=""):
    filtered = df.copy()

    filter_map = {
        "city": city,
        "country": country,
        "category": category,
    }

    for column, value in filter_map.items():
        if value:
            filtered = filtered[contains_value(filtered[column], value)]

    if search:
        mask_name = contains_value(filtered["company_name"], search)
        mask_site = contains_value(filtered["website"], search)
        filtered = filtered[mask_name | mask_site]

    return filtered.sort_values("company_name")


leads_df = load_leads()


@app.route("/")
def index():
    global leads_df

    city = request.args.get("city", "").strip()
    country = request.args.get("country", "").strip()
    category = request.args.get("category", "").strip()
    search = request.args.get("search", "").strip()
    page = request.args.get("page", 1)

    try:
        page = int(page)
        if page < 1:
            page = 1
    except (TypeError, ValueError):
        page = 1

    filtered = apply_filters(
        leads_df,
        city=city,
        country=country,
        category=category,
        search=search,
    )

    total_items = len(filtered)
    total_pages = max(1, math.ceil(total_items / ITEMS_PER_PAGE))

    if page > total_pages:
        page = total_pages

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    page_items = filtered.iloc[start:end]
    page_items = page_items.where(pd.notnull(page_items), None)

    leads = page_items.to_dict(orient="records")

    return render_template(
        "index.html",
        leads=leads,
        page=page,
        total_pages=total_pages,
        total_items=total_items,
        city=city,
        country=country,
        category=category,
        search=search,
    )


@app.route("/export")
def export():
    global leads_df

    city = request.args.get("city", "").strip()
    country = request.args.get("country", "").strip()
    category = request.args.get("category", "").strip()
    search = request.args.get("search", "").strip()

    filtered = apply_filters(
        leads_df,
        city=city,
        country=country,
        category=category,
        search=search,
    )

    csv_data = filtered.to_csv(index=False)

    response = Response(csv_data, mimetype="text/csv; charset=utf-8")
    response.headers["Content-Disposition"] = "attachment; filename=filtered_leads.csv"
    return response


if __name__ == "__main__":
    app.run(debug=True)
