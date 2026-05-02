
from fastapi import FastAPI
from app.schemas import ChurnRequest, BatchChurnRequest
from app.model_loader import load_model
from app.predict import predict_churn, predict_batch
from app.core.logger import logger
from app.errors import raise_invalid_input

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "Churn API running"}

@app.post("/predict")
def predict(data: ChurnRequest):
    try:
        logger.info(f"Input received: {data.model_dump()}")  # ✅ log input
        
        result = predict_churn(model, data)
        return {"prediction": result}

    except Exception:
        logger.warning("Invalid input received")
        raise_invalid_input()



# 🔹 Batch prediction ⭐
@app.post("/predict-batch")
def predict_batch_api(data: BatchChurnRequest):
    try:
        results = predict_batch(model, data.inputs)
        return {"predictions": results}

    except Exception:
        raise_invalid_input()




if __name__ == "__main__":
    print("running from main.py")