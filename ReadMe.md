

# Customer Churn Prediction API

## Overview

Built an end to end machine learning system to predict customer churn and expose predictions through a scalable API for real time and batch usage.

---

## Key Highlights

* Trained and compared models, improving recall from around 0.82 with logistic regression to around 0.95 using random forest
* Focused on recall to capture high risk churn customers and reduce missed cases
* Designed preprocessing and modeling pipeline to ensure consistency between training and inference

---

## System Design

* Developed REST API using FastAPI for real time and batch predictions
* Implemented input validation, logging, and error handling for reliability
* Added background task processing for non blocking operations
* Integrated basic monitoring to track prediction volume and churn trends
* Applied API versioning to support future model updates

---

## Tech Stack

Python, Pandas, Scikit learn, FastAPI, Pydantic, Uvicorn, Docker

---

## Business Impact

Enables early identification of churn risk, helping businesses take proactive retention actions and reduce revenue loss

---

## Status

Production ready ML API with modular and scalable design, ready for deployment and further extension
