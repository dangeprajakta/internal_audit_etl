def run_sql_audit_queries(conn):
    """
    Executes automated SQL audit procedures and routines to identify 
    internal control issues.
    """
    print("\n--- [ANALYZE] Executing SQL Audit Procedures ---")
    cursor = conn.cursor()
    
    # Audit Test 1: Purchase Orders exceeding approval limits
    print("\n[AUDIT TEST 1] Checking for Purchase Orders exceeding approval limits:")
    query_over_limit = """
        SELECT po_id, vendor_id, po_amount, approval_limit, 
               (po_amount - approval_limit) as excess_amount
        FROM fact_purchase_orders
        WHERE po_amount > approval_limit;
    """
    cursor.execute(query_over_limit)
    for row in cursor.fetchall():
        print(f" -> VIOLATION: PO {row[0]} for Vendor {row[1]} is ${row[2]} (Limit: ${row[3]}, Excess: ${row[4]})")

    # Audit Test 2: Duplicate Invoices / Payments
    print("\n[AUDIT TEST 2] Checking for Duplicate Invoice IDs (Potential Double Payment):")
    query_duplicates = """
        SELECT invoice_id, COUNT(*) as duplicate_count, SUM(invoice_amount) as total_paid
        FROM fact_invoices
        GROUP BY invoice_id
        HAVING COUNT(*) > 1;
    """
    cursor.execute(query_duplicates)
    for row in cursor.fetchall():
        print(f" -> VIOLATION: Invoice ID {row[0]} appears {row[1]} times. Total amount exposed: ${row[2]}")

    conn.close()