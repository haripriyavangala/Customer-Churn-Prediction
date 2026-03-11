src/train_model.py

import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from data_preprocessing import load_and_preprocess

# Load data
df = load_and_preprocess("../data/churn.csv")

X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open("../models/churn_model.pkl", "wb") as f:
    pickle.dump(model, f)
