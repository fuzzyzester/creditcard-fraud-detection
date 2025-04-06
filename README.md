
# 💳 Credit Card Fraud Detection – End-to-End ML + Power BI Project

This project presents a complete end-to-end fraud detection solution, combining machine learning, FastAPI model deployment, and interactive Power BI dashboards to identify and monitor fraudulent credit card transactions using a real-world dataset.

It demonstrates how data science and engineering can work together to create scalable, real-world applications — from preprocessing and modeling to deployment and business intelligence.

---

## Project Overview

| Stage              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Data Exploration   | Understand features, detect imbalances, and explore correlations            |
| Machine Learning   | Preprocessing, training, tuning, and evaluating multiple models             |
| Deployment         | Export model as `.pkl`, serve predictions via FastAPI, and output results   |
| Power BI Dashboard | Visualize insights, KPIs, and fraud risk for decision-making                |

---

## About the Dataset

- Source: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Total Transactions: 284,807
- Fraudulent Transactions: 492 (0.17%) – Highly imbalanced dataset

### Features
[View Feature Importance](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/FeatureImportance.png)  
![Feature Importance](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/FeatureImportance.png)

- V1 to V28: Anonymized using PCA
- Amount: Transaction value
- Time: Seconds since the first transaction
- Class: Target variable (1 = Fraud, 0 = Legitimate)

### Why PCA?

PCA anonymizes sensitive information while preserving useful patterns, enabling effective fraud detection without compromising privacy.

---

## Machine Learning Workflow

### Preprocessing

- Dropped low-impact feature: `Time`
- Scaled `Amount` using `StandardScaler`
- Separated `X` (features) and `y` (target)

### Correlation Analysis

- Strong correlations: `V14`, `V12`, `V10`
- Moderate: `V17`, `V4`, `V7`
- Weak: `Time`, `Amount`

### Handling Imbalance

Used `class_weight='balanced'` with Random Forest to emphasize rare fraud cases without oversampling.

### Models Trained

- Logistic Regression
- XGBoost
- Random Forest (Best Performer)

**Best Model Metrics:**

- Precision: 98.6%
- Recall: 96.9%
- F1 Score: 97.7%
- ROC AUC: 0.99

### Evaluation Tools

- Confusion Matrix

  
[View Confusion Matrix](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/ConfusionMatrixBestModel.png)  
![Confusion Matrix](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/ConfusionMatrixBestModel.png)

- Classification Report
- Precision-Recall Curve
- ROC-AUC Score
- 
[View Model Comparison](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/Comparison3Models.png)  
![Model Comparison](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/Comparison3Models.png)

---

## Deployment

- Exported final model as `.pkl`: `fraud_model_final.pkl`
- Created prediction CSV: `fraud_predictions.csv`
- Developed a FastAPI backend for local predictions and API access

---

## Power BI Dashboard Highlights

The dashboard translates ML predictions into actionable fraud insights for analysts and managers.

![Power BI Dashboard](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/Screenshot%202025-04-02%20113638.png)


### KPIs

- Total Transactions Checked: 56,962
- Flagged as Potential Fraud: 95
- Overall Fraud Detection Score: 0.85
- Prediction Accuracy: 100%
- Frauds Successfully Detected (%): 84%
- Correct Fraud Alerts (%): 86%

### Transaction Table (Interactive)

- Actual vs. Predicted label
- Risk level tags (Very Low, Low, Medium, High)
- Fraud probability and confidence score

### Visual Insights

- Pie chart of fraud vs. legitimate predictions
- Stacked bar chart by risk score
- Slicer control for probability thresholds and model confidence

### DAX Measures

- Dynamic KPIs implemented using `CALCULATE`, `SELECTEDVALUE`, and slicer filtering

---

## Project Learnings

### ML Takeaways

- Class Imbalance Matters: Focused on fraud despite rarity
- Beyond Accuracy: Prioritized recall and precision
- PCA Still Works: Anonymized data can retain predictive power
- Deploy Early: Model deployment adds practical value

### BI Takeaways

- Low % ≠ Low Risk: Fraud impact is high even with low occurrence
- Visual Communication: Key to stakeholder trust and decisions
- BI + ML = Trust: Combining both bridges gaps in technical understanding

---

## Future Improvements

- Live connect Power BI to FastAPI for real-time predictions
- Stream new transactions for continuous fraud detection
- Integrate case management for flagged transactions

---

## Author

**Rianna Aalto** ([fuzzyzester on GitHub](https://github.com/fuzzyzester))  
Passionate about building impactful, real-world data solutions through full-stack ML and BI integration.

---

## Project Links

- [Notebook: creditcard_fraud.ipynb](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb)
- [Dashboard: FraudRiskAnalysis.pbix](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/FraudRiskAnalysis.pbix)
- [API Script: main.py](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/main.py)
- [Model: fraud_model_final.pkl](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_model_final.pkl)
- [Predictions: fraud_predictions.csv](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_predictions.csv)
