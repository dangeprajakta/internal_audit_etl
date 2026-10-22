import sqlite3
import pandas as pd

def generate_executive_report():
    """
    Queries the SQLite data warehouse, aggregates audit findings, 
    prints an executive summary, and exports datasets for Power BI / Tableau.
    """
    print("\n--- [BI & EXECUTIVE REPORTING] Generating Executive Dashboard Summary ---")
    
    # 1. Connect to our Data Warehouse
    conn = sqlite3.connect('audit_warehouse.db')
    
    # 2. Query total financial exposure from purchase order limit violations
    query_over_limit = """
        SELECT po_id, vendor_id, po_amount, approval_limit, 
               (po_amount - approval_limit) as excess_amount
        FROM fact_purchase_orders
        WHERE po_amount > approval_limit;
    """
    df_over_limit = pd.read_sql(query_over_limit, conn)
    
    # 3. Query duplicate invoices
    query_duplicates = """
        SELECT invoice_id, COUNT(*) as duplicate_count, SUM(invoice_amount) as total_exposed
        FROM fact_invoices
        GROUP BY invoice_id
        HAVING COUNT(*) > 1;
    """
    df_duplicates = pd.read_sql(query_duplicates, conn)
    
    conn.close()
    
    # 4. Calculate Executive Summary Metrics
    total_po_exposure = df_over_limit['excess_amount'].sum() if not df_over_limit.empty else 0
    total_duplicate_exposure = df_duplicates['total_exposed'].sum() if not df_duplicates.empty else 0
    grand_total_risk = total_po_exposure + total_duplicate_exposure
    
    # 5. Print Executive Summary Table for Leadership
    print("\n==========================================")
    print("      INTERNAL AUDIT EXECUTIVE SUMMARY    ")
    print("==========================================")
    print(f" • Total PO Over-Limit Violations  : {len(df_over_limit)} items")
    print(f" • Total Duplicate Invoice Findings : {len(df_duplicates)} items")
    print(f" • Est. Total Financial Exposure    : ${grand_total_risk:,.2f}")
    print("==========================================")
    
    # 6. Export clean CSVs for Power BI / Tableau consumption
    df_over_limit.to_csv('powerbi_po_violations.csv', index=False)
    df_duplicates.to_csv('powerbi_duplicate_invoices.csv', index=False)
    print("[SUCCESS] Executive reporting tables exported to CSV for Power BI / Tableau ingestion.")
    
    return {
        "total_financial_exposure": grand_total_risk,
        "po_violations_count": len(df_over_limit),
        "duplicate_count": len(df_duplicates)
    }

if __name__ == "__main__":
    generate_executive_report()