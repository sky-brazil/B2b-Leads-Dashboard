from flask import Flask, render_template, request, Response
import pandas as pd
import math

app = Flask(__name__)

CSV_PATH = "leads.csv"
ITEMS_PER_PAGE = 20


def load_leads():
    df = pd.read_csv(CSV_PATH)
    expected_cols = [
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
    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")
    return df


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
    except ValueError:
        page = 1

    filtered = leads_df.copy()

    if city:
        filtered = filtered[filtered["city"].str.contains(city, case=False, na=False)]
    if country:
        filtered = filtered[filtered["country"].str.contains(country, case=False, na=False)]
    if category:
        filtered = filtered[filtered["category"].str.contains(category, case=False, na=False)]
    if search:
        mask_name = filtered["company_name"].str.contains(search, case=False, na=False)
        mask_site = filtered["website"].str.contains(search, case=False, na=False)
        filtered = filtered[mask_name | mask_site]

    filtered = filtered.sort_values("company_name")

    total_items = len(filtered)
    total_pages = max(1, math.ceil(total_items / ITEMS_PER_PAGE))

    if page > total_pages:
        page = total_pages

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    page_items = filtered.iloc[start:end]

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

    filtered = leads_df.copy()

    if city:
        filtered = filtered[filtered["city"].str.contains(city, case=False, na=False)]
    if country:
        filtered = filtered[filtered["country"].str.contains(country, case=False, na=False)]
    if category:
        filtered = filtered[filtered["category"].str.contains(category, case=False, na=False)]
    if search:
        mask_name = filtered["company_name"].str.contains(search, case=False, na=False)
        mask_site = filtered["website"].str.contains(search, case=False, na=False)
        filtered = filtered[mask_name | mask_site]

    filtered = filtered.sort_values("company_name")

    csv_data = filtered.to_csv(index=False)

    response = Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=filtered_leads.csv"
    return response


if __name__ == "__main__":
    app.run(debug=True)
