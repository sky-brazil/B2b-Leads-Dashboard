# B2B Lead Intelligence Dashboard (Flask)

Portfolio-grade internal tool for sales operations teams, SDR agencies, and growth partners that need fast lead qualification workflows.

## Executive Summary

This project turns a raw lead spreadsheet into a lightweight, business-friendly web app.
Users can filter by market criteria, review company records quickly, and export a campaign-ready CSV in one flow.

The goal is simple: reduce manual sorting time and accelerate outreach execution.

## Why This Matters for Clients

- **Faster qualification cycles:** your team can segment and prioritize records in seconds.
- **Lower ops overhead:** no need to manipulate CSV files manually for every campaign.
- **Reusable workflow:** ideal as a starter layer for custom CRM syncs, enrichment pipelines, or outbound tooling.

## Product Features

- Filter leads by **country**, **city**, **category**, and **free-text search**.
- Paginated lead table with clear, readable business fields.
- One-click export of the **current filtered subset**.
- Clean UI designed for internal operations usage.

## Tech Stack

- Python 3
- Flask
- Pandas
- Bootstrap 5 (CDN)

## Project Structure

```text
/workspace
├── app.py
├── leads.csv
├── requirements.txt
├── test_app.py
└── templates/
    └── index.html
```

## Local Setup

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Running Tests

```bash
python3 -m unittest -v
```

## Data Contract (`leads.csv`)

Required columns:

- `id`
- `company_name`
- `category`
- `country`
- `city`
- `address`
- `phone`
- `website`
- `rating`

If required columns are missing, the app raises a clear validation error at startup.

## HTTP Endpoints

- `GET /`  
  Renders the dashboard with filter and pagination support.

- `GET /export`  
  Returns a downloadable CSV containing only the currently filtered records.

## Commercial Positioning

This repository is intentionally structured as a practical delivery sample for B2B data and sales-ops engagements.
It demonstrates:

- clean backend logic,
- straightforward UI implementation,
- export-focused business utility,
- and basic automated route validation.

## Next Production-Ready Enhancements

- Authentication and role-based access
- CRM integrations (HubSpot, Pipedrive, Salesforce)
- Saved filter presets for campaigns
- Data enrichment hooks (Clearbit, Apollo, custom APIs)
- Docker and cloud deployment profile

---

If you are evaluating this repository from an outsourcing or Upwork perspective, this codebase is designed to show clear communication, pragmatic implementation, and business-oriented product thinking.
