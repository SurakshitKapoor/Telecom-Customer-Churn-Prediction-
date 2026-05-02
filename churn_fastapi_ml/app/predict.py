

import pandas as pd

# def predict_churn(model, data):
#     df = pd.DataFrame([data.dict()])
#     prediction = model.predict(df)[0]
#     return int(prediction)


import pandas as pd
from app.core.logger import logger
from app.errors import raise_model_error

def predict_churn(model, data):
    try:
        logger.info("Making pydantic data into dataframe")
        df = pd.DataFrame([data.model_dump()])

        logger.info("running the model for prediction!")
        prediction = model.predict(df)[0]

        logger.info(f"Prediction made: {prediction} | Input: {data}")

        return int(prediction)

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise_model_error()



# predict for multiple inputs
def predict_batch(model, data_list):
    try:
        df = pd.DataFrame([item.model_dump() for item in data_list])

        predictions = model.predict(df).tolist()

        logger.info(f"Batch Prediction: {predictions}")
        return predictions

    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        raise_model_error()