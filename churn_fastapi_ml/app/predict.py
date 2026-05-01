

import pandas as pd

def predict_churn(model, data):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return int(prediction)
