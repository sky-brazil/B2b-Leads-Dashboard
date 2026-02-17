import math

import pandas as pd
from flask import Flask, Response, render_template, request

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


def load_leads() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    missing = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")
    return df


def get_filters() -> dict[str, str]:
    return {
        "city": request.args.get("city", "").strip(),
        "country": request.args.get("country", "").strip(),
        "category": request.args.get("category", "").strip(),
        "search": request.args.get("search", "").strip(),
    }


def apply_filters(df: pd.DataFrame, filters: dict[str, str]) -> pd.DataFrame:
    filtered = df.copy()

    for column in ("city", "country", "category"):
        query = filters[column]
        if query:
            filtered = filtered[filtered[column].str.contains(query, case=False, na=False)]

    search_query = filters["search"]
    if search_query:
        company_name_match = filtered["company_name"].str.contains(search_query, case=False, na=False)
        website_match = filtered["website"].str.contains(search_query, case=False, na=False)
        filtered = filtered[company_name_match | website_match]

    return filtered.sort_values("company_name")


leads_df = load_leads()


@app.route("/")
def index():
    filters = get_filters()
    page = request.args.get("page", default=1, type=int) or 1
    if page < 1:
        page = 1

    filtered = apply_filters(leads_df, filters)
    total_items = len(filtered)
    total_pages = max(1, math.ceil(total_items / ITEMS_PER_PAGE))

    if page > total_pages:
        page = total_pages

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    page_items = filtered.iloc[start:end]

    return render_template(
        "index.html",
        leads=page_items.to_dict(orient="records"),
        page=page,
        total_pages=total_pages,
        total_items=total_items,
        **filters,
    )


@app.route("/export")
def export():
    filtered = apply_filters(leads_df, get_filters())
    csv_data = filtered.to_csv(index=False)
    response = Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=filtered_leads.csv"
    return response


if __name__ == "__main__":
    app.run(debug=True)
