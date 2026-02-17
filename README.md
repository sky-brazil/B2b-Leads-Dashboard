# B2B Leads Dashboard (Flask)

## Executive Summary

This project is a lightweight **B2B lead qualification dashboard** designed for sales teams, SDRs, and lead generation agencies.
It transforms a raw CSV list of companies into a clean, searchable workspace where users can segment leads and export outreach-ready lists in seconds.

For an Upwork portfolio, this demo showcases practical value: **fast filtering, better targeting, and cleaner handoff to outbound campaigns**.

## Business Problem

Most lead lists arrive as flat spreadsheets with limited usability.
Without a clear interface, teams lose time filtering by location or niche and struggle to prioritize who to contact first.

## Solution Delivered

The app reads `leads.csv` and provides:

- Multi-field filtering (country, city, category, keyword).
- Paginated and responsive lead table for daily operational use.
- One-click CSV export based on current filters.
- Simple UX optimized for speed in sales workflows.

## Tech Stack

- Python 3
- Flask
- Pandas
- Bootstrap 5 (CDN)
- CSV as data source (easy to replace later with DB/API)

## Quick Start

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

Then open: `http://127.0.0.1:5000`

## CSV Schema (Required Columns)

- `id`
- `company_name`
- `category`
- `country`
- `city`
- `address`
- `phone`
- `website`
- `rating`

## Project Structure

```text
/workspace
  app.py
  leads.csv
  requirements.txt
  templates/
    index.html
  README.md
```

## Upwork Positioning

This demo can be positioned as:

1. **Lead Management MVP** for agencies and sales teams.
2. **Custom filtering/export tool** before CRM upload.
3. **Internal operations dashboard** for SDR assistants and VA teams.

### Natural Paid Extensions

- CRM integration (HubSpot, Pipedrive, Salesforce).
- Google Sheets sync and scheduled imports.
- Lead enrichment (emails, social profiles, firmographics).
- User login, role permissions, and activity logs.
- REST API to ingest leads from scraping pipelines.

## Recent Improvements Applied

- Fixed Flask template structure to prevent `TemplateNotFound` errors.
- Made text filtering safer and more stable using literal matching (`regex=False`).
- Standardized UI copy in professional English for client-facing demos.
