
import json
from datetime import datetime

def save_prediction(data, prediction):
    record = {
        "timestamp": str(datetime.now()),
        "input": data,
        "prediction": prediction
    }

    with open("logs/predictions.json", "a") as f:
        f.write(json.dumps(record) + "\n")