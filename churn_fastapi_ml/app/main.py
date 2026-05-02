
from fastapi import FastAPI, BackgroundTasks
from app.schemas import ChurnRequest, BatchChurnRequest
from app.model_loader import load_model
from app.predict import predict_churn, predict_batch
from app.core.logger import logger
from app.errors import raise_invalid_input
from app.tasks.background_tasks import save_prediction

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "Churn API running"}

@app.post("/predict")
def predict(data: ChurnRequest, background_tasks: BackgroundTasks):
    try:
        logger.info(f"Input received: {data.model_dump()}")  # ✅ log input
        
        result = predict_churn(model, data)

        # runs async
        background_tasks.add_task(
            save_prediction,
            data.model_dump(),
            result
        )

        return {"prediction": result}

    except Exception:
        logger.warning("Invalid input received")
        raise_invalid_input()



# 🔹 Batch prediction ⭐
@app.post("/predict-batch")
def predict_batch_api(data: BatchChurnRequest, background_tasks: BackgroundTasks):
    try:
        results = predict_batch(model, data.inputs)

        # ✅ save each record in background
        for inp, res in zip(data.inputs, results):
            background_tasks.add_task(
                save_prediction,
                inp.model_dump(),
                res
            )

            
        return {"predictions": results}

    except Exception:
        raise_invalid_input()




if __name__ == "__main__":
    print("running from main.py")