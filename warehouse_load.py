import sqlite3

def load_to_warehouse(vendors, pos, invoices):
    """
    Simulates loading cleaned ERP data into an enterprise data warehouse 
    (like Snowflake) using a relational database (SQLite).
    """
    print("\n--- [LOAD] Loading data into Data Warehouse Staging Tables ---")
    
    conn = sqlite3.connect('audit_warehouse.db')
    
    vendors.to_sql('dim_vendors', conn, if_exists='replace', index=False)
    pos.to_sql('fact_purchase_orders', conn, if_exists='replace', index=False)
    invoices.to_sql('fact_invoices', conn, if_exists='replace', index=False)
    
    print("[SUCCESS] Tables loaded into Warehouse: dim_vendors, fact_purchase_orders, fact_invoices")
    return conn