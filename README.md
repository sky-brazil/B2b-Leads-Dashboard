# B2B Leads Dashboard (Flask)

## Problem

Sales teams and marketing agencies often receive company lists as messy spreadsheets or raw data scraped from public business directories (Yellow Pages–style).  
Without a clean view, it is hard to filter by city, niche, and quickly decide which leads to contact first.

## Solution

This project is a **mini web dashboard built with Flask** that reads a `leads.csv` file with local businesses and allows you to:

- Filter leads by country, city, category, and free text (company name or domain).
- View the results in a responsive, paginated table.
- Export a CSV containing only the currently filtered leads, ready for outreach campaigns.

It’s a simple internal tool example for sales teams, SDRs, and agencies working with B2B lead generation.

## Tech stack

- Python 3.x  
- Flask  
- Bootstrap 5 (via CDN)  
- CSV as the data source

## Project structure

```text
b2b_leads_dashboard/
  app.py
  leads.csv
  requirements.txt
  templates/
    index.html

