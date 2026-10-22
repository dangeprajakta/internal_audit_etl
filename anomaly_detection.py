import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(invoices):
    """
    Uses an Isolation Forest machine learning model to detect 
    unusual/anomalous invoices based on transaction amounts.
    """
    print("\n--- [ML ANALYTICS] Running Isolation Forest Anomaly Detection ---")
    
    # 1. Prepare data (Machine learning models require numbers)
    X = invoices[['invoice_amount']].fillna(0)
    
    # 2. Initialize the Isolation Forest Model
    model = IsolationForest(contamination=0.2, random_state=42)
    
    # 3. Train the model and predict anomalies (-1 means outlier, 1 means normal)
    invoices['anomaly_score'] = model.fit_predict(X)
    
    # 4. Filter out the anomalies
    anomalies = invoices[invoices['anomaly_score'] == -1]
    
    print(f"[ML RESULTS] Scanned {len(invoices)} transactions. Flagged {len(anomalies)} statistical anomalies.")
    
    for index, row in anomalies.iterrows():
        print(f" -> ML ALERT: Invoice ID {row['invoice_id']} for ${row['invoice_amount']} was flagged as a statistical outlier!")
        
    return invoices