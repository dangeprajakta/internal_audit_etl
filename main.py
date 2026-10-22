# Import functions from our modular script files
from extract import extract_erp_data
from profile_data import profile_and_validate_data
from warehouse_load import load_to_warehouse
from audit_queries import run_sql_audit_queries
from anomaly_detection import detect_anomalies
from nlp_parser import scan_vendor_contracts
from automation_alerts import trigger_automated_remediation
from executive_report import generate_executive_report



def main():
    print("==========================================")
    print(" STARTING ENTERPRISE AUDIT ETL PIPELINE   ")
    print("==========================================")
    
    # Step 1: Extract
    vendors, pos, invoices = extract_erp_data()
    
    # Step 2: Profile & Validate Quality
    audit_flags = profile_and_validate_data(vendors, pos, invoices)
    
    # Step 3: Load into Data Warehouse
    warehouse_conn = load_to_warehouse(vendors, pos, invoices)
    
    # Step 4: Execute Automated Audit Procedures
    run_sql_audit_queries(warehouse_conn)

    #Step 5: Run Machine Learning Anomaly Detection (NEW!)
    invoices_with_ml = detect_anomalies(invoices)

    # Step 6: Run NLP Contract Screening (NEW!)
    nlp_results = scan_vendor_contracts()

    # Step 7: Trigger Automated Continuous Monitoring Alerts & RPA Remediation (NEW!)
    remediation_tickets = trigger_automated_remediation(nlp_results)

    # Step 8: Generate Executive Summary & Power BI Exports (NEW!)
    executive_metrics = generate_executive_report()
    
    print("\n==========================================")
    print(" PIPELINE EXECUTION COMPLETE SUCCESSFULLY ")
    print("==========================================")

if __name__ == "__main__":
    main()