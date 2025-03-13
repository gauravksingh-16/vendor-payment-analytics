# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ml_models import predict_payment_delay, detect_anomaly
from blockchain import record_payment_transaction

app = FastAPI(title="AI-Driven Payment Prediction & Anomaly Detection")

# Pydantic model for incoming payment data
class PaymentData(BaseModel):
    transaction_id: str
    amount: float
    vendor: str
    timestamp: str  # ISO formatted string

@app.get("/predict-payment-delay")
async def predict_payment_delay_endpoint(transaction_id: str):
    # In practice, retrieve transaction details from your data store.
    dummy_data = {
        "transaction_id": transaction_id,
        "amount": 100.0,
        "timestamp": "2025-03-14T12:00:00"
    }
    predicted_delay = predict_payment_delay(dummy_data)
    return {"transaction_id": transaction_id, "predicted_delay_days": predicted_delay}

@app.get("/detect-anomaly")
async def detect_anomaly_endpoint(transaction_id: str):
    dummy_data = {
        "transaction_id": transaction_id,
        "amount": 100.0,
        "timestamp": "2025-03-14T12:00:00"
    }
    anomaly_flag = detect_anomaly(dummy_data)
    return {"transaction_id": transaction_id, "anomaly_detected": anomaly_flag}

@app.post("/vendor-payment")
async def vendor_payment(payment: PaymentData):
    try:
        tx_receipt = record_payment_transaction(payment.vendor, payment.amount, payment.transaction_id)
        return {"status": "Payment recorded on blockchain", "tx_receipt": tx_receipt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
