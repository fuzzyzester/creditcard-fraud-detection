
# 💳 Credit Card Fraud Detection & Risk Insights

This end-to-end project combines **Machine Learning**, **Model Deployment**, and **Power BI Visualization** to build a real-world **Credit Card Fraud Detection** system. It uses a public dataset of anonymized credit card transactions and aims to:

- Detect fraudulent transactions using a Machine Learning pipeline  
- Provide fraud risk insights with an interactive Power BI Dashboard  
- Deploy the model using FastAPI for integration or future real-time applications

---

##  Overview

| Component | Description |
|----------|-------------|
|  Data | Credit card transactions dataset (284,807 transactions, 492 fraud cases) |
|  ML Model | Random Forest Classifier with hyperparameter tuning |
|  Deployment | FastAPI model server with `.pkl` model |
|  Dashboard | Power BI report with fraud insights and risk levels |

---

##  Repository Structure

```bash
├── creditcard_fraud.ipynb           # ML pipeline (Exploration, Training, Evaluation)
├── fraud_model_final.pkl            # Final serialized model
├── fraud_predictions.csv            # Model predictions with probabilities
├── powerBIdashboard_CreditCard_fraud_detection.png # Dashboard Screenshot
├── app/                             # FastAPI deployment files
└── README.md                        # This file
```

---

##  Machine Learning Pipeline

### 1.  Data Preprocessing
- Removed null values and duplicates
- Scaled `Amount` feature using StandardScaler
- Addressed **class imbalance** using **undersampling**

### 2.  Model Training
- Algorithm: **Random Forest Classifier**
- Hyperparameter tuning using `GridSearchCV`
- Evaluation Metrics:
  - Accuracy: `1.00`
  - Precision: `0.84`
  - Recall: `0.86`
  - ROC-AUC: `0.85`

### 3.  Evaluation
- Model achieved perfect accuracy on validation
- ROC Curve used for threshold optimization
- Exported predictions with fraud probabilities to `fraud_predictions.csv`

---

##  Model Deployment

- Serialized the best model as `fraud_model_final.pkl`
- Built a **FastAPI** endpoint to load and serve predictions
- You can test or extend this using tools like **Postman**, or integrate with **Power BI API**

```python
# Sample FastAPI code snippet
@app.post("/predict")
def predict(data: TransactionData):
    prediction = model.predict([data.features])
    return {"prediction": prediction}
```

---

##  Power BI Dashboard

###  Dashboard Title:
**CREDIT CARD FRAUD DETECTION & RISK INSIGHTS**

### 🔹 Key Features:
-  **KPI Cards**:
  - Total Transactions Checked: 56,962
  - Flagged as Potential Fraud: 95
  - Prediction Accuracy: 1.00
  - Overall Fraud Detection Score: 0.85
  - Correct Fraud Alerts (%): 0.86
  - Frauds Successfully Detected (%): 0.84

-  **Slicer (Threshold Values)**:
  - Adjustable threshold for fraud probability (0.10 to 0.98)
  - Connected to dynamic measures like Accuracy, Precision, Recall (via `ThresholdTable`)

-  **Transaction Table**:
  - Shows each transaction with actual vs predicted labels, fraud probability, risk level

-  **Fraud Risk Analysis**:
  - Pie Chart: Predicted Fraud vs Legitimate
  - Bar Chart: Transactions by Risk Level & Probability Ranges

###  Dashboard Insight:
The model confidently classifies fraudulent transactions while minimizing false positives. Legitimate transactions dominate the dataset, but the model effectively identifies high-risk outliers. Users can interactively filter transactions based on fraud probability thresholds.

![Dashboard Screenshot](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png)

---

##  Key Learnings

- Successfully handled **imbalanced datasets**
- Learned how to tune, evaluate, and serialize ML models
- Developed a working **FastAPI backend** for real-world deployment
- Integrated machine learning results into an **interactive Power BI report**
- Learned to build **dynamic measures and visuals** with user-driven slicers

---

##  Future Improvements

-  Integrate FastAPI with Power BI using APIs for real-time predictions
-  Add user authentication and input logging in deployment
-  Train with SMOTE or other oversampling for better fraud recall
-  Containerize the app using Docker for cloud deployment
-  Add time-based patterns in fraud risk (timestamp analysis)
-  Add multi-language support and international currency formatting

---

##  Important Links

| Type | Link |
|------|------|
|  Notebook | [creditcard_fraud.ipynb](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb) |
|  Model File | [fraud_model_final.pkl](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_model_final.pkl) |
|  Predictions CSV | [fraud_predictions.csv](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_predictions.csv) |
|  Dashboard Image | [Dashboard Screenshot](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png) |

---

##  Let's Connect

If you're interested in how this model was built, deployed, or used in Power BI — feel free to [connect with me on GitHub](https://github.com/fuzzyzester)!

---

> This project showcases how data science, deployment, and business intelligence come together to create meaningful, actionable insights.

