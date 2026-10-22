import pandas as pd

def profile_and_validate_data(vendors, pos, invoices):
    """
    Profiles raw ERP datasets for schema completeness, null values, 
    duplicates, and sequence gaps.
    """
    print("\n--- [TRANSFORM & PROFILE] Running Data Quality Checks ---")
    audit_flags = {}

    # 1. Schema Completeness Check
    expected_invoice_cols = {'invoice_id', 'po_id', 'vendor_id', 'invoice_amount', 'invoice_date'}
    missing_cols = expected_invoice_cols - set(invoices.columns)
    if missing_cols:
        print(f"[FAIL] Schema Error: Missing columns in Invoices: {missing_cols}")
    else:
        print("[PASS] Schema Completeness: All expected invoice columns present.")

    # 2. Null Value Profiling
    null_counts = invoices.isnull().sum()
    print("\n[PROFILING] Null value counts per column in Invoices:")
    print(null_counts)
    audit_flags['null_invoices'] = null_counts['po_id']

    # 3. Duplicate Record Check
    duplicate_count = invoices.duplicated(subset=['invoice_id']).sum()
    print(f"\n[DUPLICATE CHECK] Found {duplicate_count} duplicate invoice ID records.")
    audit_flags['duplicate_invoices'] = duplicate_count

    # 4. Sequence Gap Check
    invoices_sorted = invoices.sort_values('invoice_id').drop_duplicates(subset=['invoice_id'])
    min_inv = invoices_sorted['invoice_id'].min()
    max_inv = invoices_sorted['invoice_id'].max()
    expected_range = set(range(min_inv, max_inv + 1))
    actual_invoices = set(invoices_sorted['invoice_id'])
    missing_invoices = sorted(list(expected_range - actual_invoices))
    
    print(f"\n[SEQUENCE CHECK] Invoice ID sequence range: {min_inv} to {max_inv}")
    if missing_invoices:
        print(f"[ALERT] Missing sequential invoice numbers detected: {missing_invoices}")
    else:
        print("[PASS] No sequence gaps found in invoice numbers.")
    audit_flags['missing_sequence'] = missing_invoices

    # 5. Referential Integrity Check
    orphaned_invoices = invoices[~invoices['vendor_id'].isin(vendors['vendor_id'])]
    if not orphaned_invoices.empty:
        print(f"\n[ALERT] Referential Integrity Failure: {len(orphaned_invoices)} orphaned invoices found.")
    
    return audit_flags