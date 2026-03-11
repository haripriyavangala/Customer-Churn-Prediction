src/predict.py

import pickle
import pandas as pd

# Load trained model
with open("../models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example customer data
sample = pd.DataFrame({
    "tenure":[5],
    "MonthlyCharges":[70]
})

prediction = model.predict(sample)

print("Churn Prediction:", prediction)
