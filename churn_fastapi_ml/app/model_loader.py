

# import joblib
# import os

# def load_model():
#     base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
#     model_path = os.path.join(base_dir, "models", "churn_model.pkl")
#     return joblib.load(model_path)

import joblib
from app.core.config import settings

def load_model():
    return joblib.load(settings.model_path)