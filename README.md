# 📊 Internal Procurement Audit & Compliance Dashboard

An end-to-end automated data pipeline and executive Power BI dashboard built to detect purchase order (PO) over-limit violations and duplicate vendor invoice risks.

---

## 📌 Project Overview
In large corporate procurement systems, manual sampling often fails to flag non-compliant transactions and fraudulent duplicate payments. 

This project implements an automated **ETL pipeline** and **executive reporting solution** that:
1. Ingests procurement and invoice transactional records.
2. Applies compliance and validation rules (flagging PO amounts exceeding approval thresholds and duplicate invoice signatures).
3. Exports prioritized risk metrics into structured exception logs.
4. Visualizes high-risk financial exposure for executive auditors using an interactive Power BI dashboard.

---

## 🛠️ Tech Stack & Tools
* **Programming & ETL:** Python (`pandas`, `sqlite3`)
* **Database Querying:** SQL / SQLite
* **Business Intelligence:** Power BI Desktop
* **Version Control:** Git, GitHub, VS Code

---

## ⚙️ Data Pipeline Architecture

```text
[ Raw Procurement & Invoice Data ]
              │
              ▼
    [ SQLite Data Warehouse ]
              │
              ▼
   [ Python Validation Script ]
 ┌────────────┴────────────┐
 ▼                         ▼
PO Over-Limit          Duplicate Invoice
 Violation Rules         Detection Rules
 └────────────┬────────────┘
              ▼
  [ CSV Exception Exports ]
              │
              ▼
  [ Executive Power BI Dashboard ]

Key Dashboard Features
Headline Executive Metrics: Instant visibility into total financial risk exposure across over-limit POs and duplicate invoices.

Vendor Risk Breakdown: Clustered bar chart identifying rogue vendors driving the highest compliance overages.

Audit Exception Log: Itemized table detailing exact invoice_id transactions, duplicate occurrence counts, and individual exposure amounts.

Interactive Filtering: Dynamic vendor slicer allowing auditors to isolate individual vendor profiles across all visual cards and tables.

📁 Repository Structure
├── data/                         # Source datasets and database files
├── scripts/
│   └── audit_pipeline.py         # Python ETL and validation script
├── powerbi_po_violations.csv     # Exported PO over-limit exception data
├── powerbi_duplicate_invoices.csv# Exported duplicate invoice exception data
├── Audit_Executive_Summary.pbix  # Power BI report file
├── README.md                     # Project documentation
└── .gitignore                    # Local environment and cache exclusion file

View the Power BI Report
Open Audit_Executive_Summary.pbix in Power BI Desktop to inspect the layout, data model, and interactive visual features.
