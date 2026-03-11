# Customer Churn Prediction using Machine Learning

## Project Overview
Customer churn refers to customers leaving a company or stopping the use of its services. 
This project builds a Machine Learning model to predict whether a customer is likely to churn based on historical telecom customer data.

Predicting churn helps companies take preventive actions such as offering discounts or improving services to retain customers.

---

## Problem Statement
Telecommunication companies often face customer churn, which affects revenue and growth.

The goal of this project is to build a predictive model that can classify customers into:
- Churn (Customer will leave)
- Not Churn (Customer will stay)

---

## Dataset
Dataset used: **Telco Customer Churn Dataset**

Source: Kaggle  
https://www.kaggle.com/blastchar/telco-customer-churn

### Dataset Features
The dataset contains information such as:

| Feature | Description |
|------|------|
| tenure | Number of months customer stayed |
| MonthlyCharges | Monthly subscription charges |
| TotalCharges | Total amount paid by customer |
| Contract | Type of contract |
| PaymentMethod | Payment type |
| InternetService | Type of internet service |
| Churn | Target variable (Yes / No) |

---

## Project Workflow

### 1 Data Collection
The dataset is downloaded from Kaggle and stored in the `data/` folder.

---

### 2 Data Preprocessing
Data cleaning and transformation steps include:

- Removing unnecessary columns
- Handling missing values
- Converting categorical variables into numerical values
- Feature encoding using one-hot encoding

This step ensures the dataset is ready for machine learning algorithms.

---

### 3 Exploratory Data Analysis (EDA)
EDA helps understand the patterns in the dataset.

Some analysis performed:
- Churn distribution
- Relationship between monthly charges and churn
- Contract type vs churn rate

Example visualization:

python
sns.countplot(x="Churn", data=df)

---

### 4 Feature Engineering
Feature engineering prepares the dataset for machine learning models by converting categorical variables into numerical format and handling missing values.

---

### 5 Train-Test Split

The dataset is divided into training and testing sets so that the model can be evaluated on unseen data.

---

### 6 Model Training

A Logistic Regression model is trained to classify whether a customer will churn or not.

---

### 7 Model Prediction

The trained model predicts churn for the testing dataset.

---

### 8 Model Evaluation

Model performance is evaluated using accuracy and classification metrics

---

### 9 Saving the Model

The trained model is saved using the pickle library for future predictions.

---

### 10 Using the Saved Model

The saved model can be loaded and used to predict churn for new customers.

---
<img width="588" height="358" alt="image" src="https://github.com/user-attachments/assets/c984341c-7b92-464f-989d-23dd50f3b729" />

