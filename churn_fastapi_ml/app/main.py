
from fastapi import FastAPI
from app.schemas import ChurnRequest
from app.predict import predict_churn
from app.model_loader import load_model


app = FastAPI(
    title="Telecom Churn Prediction API",
    description="Predict customer churn and enable retention campaigns",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Churn Prediction API"}

@app.get("/health")
def health():
    return {"status": "ok"}


# gtting the model
model = load_model()

@app.post("/predict")
def predict(data: ChurnRequest):
    result = predict_churn(model, data)
    return {"prediction": result}




if __name__ == "__main__":
    print("running from main.py")