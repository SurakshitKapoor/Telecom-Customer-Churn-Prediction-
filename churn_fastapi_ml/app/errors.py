

from fastapi import HTTPException

# error handling for incorrect inputs
def raise_invalid_input():
    raise HTTPException(status_code=400, detail="Invalid input data")

# error handling when model strucks
def raise_model_error():
    raise HTTPException(status_code=500, detail="Model prediction failed")