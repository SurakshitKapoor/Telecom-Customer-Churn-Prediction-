

from pydantic import BaseModel
from typing import List

# for ingle inputs
class ChurnRequest(BaseModel):
    Gender: str
    SeniorCitizen: int          # 0 or 1
    Partner: str                # Yes/No
    Dependents: str             # Yes/No
    Tenure: int
    PhoneService: str           # Yes/No
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str       # Yes/No
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


# for multiple inputs
class BatchChurnRequest(BaseModel):
    inputs: List[ChurnRequest]