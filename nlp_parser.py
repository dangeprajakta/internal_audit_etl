import os
import pdfplumber

def scan_vendor_contracts():
    """
    Reads real vendor PDF contracts from the 'contracts' folder 
    and applies NLP keyword classification to identify compliance risks.
    """
    print("\n--- [NLP ANALYTICS] Scanning Real Vendor PDF Contracts ---")
    
    # Define high-risk compliance keywords
    risk_keywords = {
        "non_compliant_terms": ["immediate", "net 0", "net 15", "upon receipt"],
        "financial_penalties": ["penalty", "interest", "late fee", "surcharge"],
        "governance_risks": ["automatic renewal", "waiver", "exclusive"]
    }
    
    # Path to the folder containing your PDF contracts
    pdf_folder = "contracts"
    
    # Check if the folder exists
    if not os.path.exists(pdf_folder):
        print(f"[ERROR] The folder '{pdf_folder}' does not exist. Please create it and add your PDF.")
        return []

    flagged_contracts = []
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    if not pdf_files:
        print(f"[WARNING] No PDF files found inside '{pdf_folder}' folder.")
        return []

    # Loop through every PDF file in the folder
    for filename in pdf_files:
        file_path = os.path.join(pdf_folder, filename)
        
        # --- 1. EXTRACT TEXT FROM THE REAL PDF ---
        contract_text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        contract_text += text + "\n"
            print(f"[INFO] Successfully read text from: {filename}")
        except Exception as e:
            print(f"[ERROR] Could not read {filename}: {e}")
            continue
        
        # --- 2. RUN NLP KEYWORD CLASSIFICATION ---
        text_lower = contract_text.lower()
        found_risks = {}
        
        for category, keywords in risk_keywords.items():
            matches = [kw for kw in keywords if kw in text_lower]
            if matches:
                found_risks[category] = matches
                
        # --- 3. TRIGGER AUDIT ALERTS ---
        if found_risks:
            flagged_contracts.append({
                "contract": filename,
                "risks": found_risks
            })
            print(f" -> NLP ALERT: '{filename}' contains high-risk clauses: {found_risks}")
        else:
            print(f" -> [PASS] '{filename}' contract terms are fully compliant.")
            
    return flagged_contracts

if __name__ == "__main__":
    scan_vendor_contracts()