import pandas as pd

def extract_erp_data():
    """
    Simulates extracting raw transactional data from an ERP system 
    via API endpoints or batch files.
    """
    print("--- [EXTRACT] Fetching raw ERP data ---")
    
    vendors = pd.DataFrame({
        'vendor_id': [101, 102, 103, 104, 105],
        'vendor_name': ['Alpha Corp', 'Beta Logistics', 'Gamma Supplies', 'Delta Tech', 'Epsilon Services'],
        'risk_rating': ['Low', 'Medium', 'High', 'Low', 'Medium'],
        'is_active': [True, True, True, False, True]
    })
    
    pos = pd.DataFrame({
        'po_id': [5001, 5002, 5003, 5004, 5005, 5006],
        'vendor_id': [101, 102, 101, 103, 104, 102],
        'po_amount': [15000.00, 4500.50, 120000.00, 890.00, 32000.00, 5400.00],
        'approval_limit': [20000.00, 5000.00, 50000.00, 1000.00, 30000.00, 5000.00]
    })
    
    invoices = pd.DataFrame({
        'invoice_id': [1001, 1002, 1003, 1005, 1006, 1006, 1008], 
        'po_id': [5001, 5002, 5003, 5004, 5005, 5005, None], 
        'vendor_id': [101, 102, 101, 103, 104, 104, 999], 
        'invoice_amount': [15000.00, 4500.50, 120000.00, 890.00, 32000.00, 32000.00, 500.00],
        'invoice_date': ['2026-01-10', '2026-01-12', '2026-01-15', '2026-01-18', '2026-01-20', '2026-01-20', '2026-01-22']
    })
    
    print(f"Extracted: {len(vendors)} vendors, {len(pos)} POs, {len(invoices)} invoices records.")
    return vendors, pos, invoices