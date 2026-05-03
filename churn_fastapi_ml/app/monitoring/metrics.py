

metrics_data = {
    "total": 0,
    "churn": 0,
    "prob_sum": 0.0
}

def update_metrics(prediction, probability):
    metrics_data["total"] += 1
    metrics_data["prob_sum"] += probability

    if prediction == 1:
        metrics_data["churn"] += 1


def get_metrics():
    total = metrics_data["total"]
    churn = metrics_data["churn"]

    return {
        "total_predictions": total,
        "churn_predictions": churn,
        "churn_rate": churn / total if total else 0,
        "avg_probability": metrics_data["prob_sum"] / total if total else 0
    }


# it does:->
# Stores stats in memory
# Updates on each prediction
# Calculates simple metrics