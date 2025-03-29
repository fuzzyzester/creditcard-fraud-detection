
# 💳 Credit Card Fraud Detection – End-to-End ML + Power BI Project

This project presents a complete end-to-end fraud detection solution, combining machine learning, FastAPI model deployment, and interactive Power BI dashboards to identify and monitor fraudulent credit card transactions using a real-world dataset.

It covers the full cycle—from data preprocessing and modeling to API deployment and business intelligence reporting—demonstrating how data science and engineering can work together to create scalable, real-world applications.

With fraudulent transactions making up only 0.17% of the dataset, handling highly imbalanced data was a core challenge—requiring careful model selection and evaluation to ensure reliable predictions.

---

##  Project Overview

| Stage | Description |
|-------|-------------|
|  Data Exploration | Understand the features, detect imbalances, and explore correlations |
|  Machine Learning | Preprocessing, training, tuning, and evaluating multiple models |
|  Deployment | Export final model as `.pkl`, convert predictions to CSV, and enable integration |
|  Power BI Dashboard | Visualize insights, KPIs, and fraud trends for business decision-making |

---

##  About the Dataset

- Source: Kaggle Credit Card Fraud Dataset
- Transactions: 284,807
- Fraud Cases: 492 (~0.17%) → Highly imbalanced
### Features:
- V1 to V28: anonymized using PCA (Principal Component Analysis)
- Amount: transaction amount
- Time: seconds elapsed since the first transaction
- Class: target variable (1 = fraud, 0 = non-fraud)

### Why PCA?

PCA anonymizes sensitive information while preserving trends and patterns. This keeps user data secure but still useful for fraud detection. V1 to V28 are transformed features that contain the underlying relationships, even if we don't know their original meanings.

---

##  Machine Learning Process

 Check the full code here: [creditcard_fraud.ipynb](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb)

###  Preprocessing
- Dropped irrelevant features (`Time`)
- Scaled `Amount` using `StandardScaler`
- Separated `X` (features) and `y` (target: fraud or not)

###  Correlation Heatmap 
- **V14, V12, V10**: Strong negative correlation with fraud → likely strong indicators
- **V17, V4, V7**: Mild correlations
- **Time**: Very weak → Dropped
- **Amount**: Low correlation → Still kept after scaling

### Addressing Class Imbalance
Instead of oversampling or undersampling, I leveraged class_weight='balanced' in our Random Forest model. This allowed the model to give more focus to rare fraud cases without artificially changing the dataset size—ensuring better generalization and avoiding overfitting.

###  Models Trained
- Logistic Regression
- Random Forest ✅ (Best)
- XGBoost

###  Best Model: Random Forest
- Precision: **98.6%**
- Recall: **96.9%**
- F1 Score: **97.7%**
- ROC AUC: **0.99**

###  Evaluation
- Confusion Matrix & Classification Report
- ROC-AUC Score
- Precision-Recall Curve
- Focus on minimizing **False Negatives** (fraud marked as safe)

---

## 🛠️ Deployment

-  Final model saved as `.pkl`:  
  [fraud_model_final.pkl](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_model_final.pkl)

-  Predictions exported to `.csv`:  
  [fraud_predictions.csv](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_predictions.csv)

-  FastAPI backend built for local prediction and API integration (Power BI / future app-ready)

---

##  Power BI Dashboard

 [View Dashboard](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/Creditcardfraudanalysis_dashboard.png)

###  Features

- KPIs for:
  - Total Transactions
  - Detected Frauds
  - Fraud % (based on predictions)
- Visuals:
  - Donut chart for fraud vs. non-fraud
  - Trend lines for fraud over time
  - Top/Bottom amounts by fraud class
  - Dynamic table of transactions
- Interactive Slicer:
  - Filter by prediction result or amount bracket

> ℹ Note: In the KPI cards, static measures were used. To fully enable dynamic interactivity with slicers, consider converting them to **dynamic measures** using `CALCULATE` + `SELECTEDVALUE`.


###  KPI Card Note
Initial version used non-dynamic measures, which caused them not to respond to slicers. To fix this:
1. Create measures using DAX (e.g., `Total_Frauds = CALCULATE(COUNTROWS(...), Class = 1)`)
2. Replace static fields with these measures

---

##  Project Learnings and Takeaways


- Practical experience in handling real-world **imbalanced data**
- Choosing and tuning ML models with a business impact in mind
- Deploying models for **reusable predictions**
- Communicating results visually through **Power BI**
- Handling **data anonymization** and transforming scaled features

###  ML Takeaways
| Insight | Description |
|--------|-------------|
|  **Class Imbalance Matters** | Fraud is rare. Handling imbalance is key. |
|  **Beyond Accuracy** | Precision & Recall matter more than accuracy in fraud detection. |
|  **PCA Still Effective** | Even anonymized features hold predictive patterns. |
|  **API Deployment** | Adds real-world usability for fraud prediction tools. |



###  Power BI Takeaways
| Insight | Description |
|--------|-------------|
|  **Low % ≠ Low Risk** | Fraud costs are high even if frequency is low. |
|  **Explain Visually** | Managers need clear, actionable visuals. |
|  **Confirm ML with BI** | Seeing ML patterns visually boosts trust. |

---

##  Future Improvements

- Switch KPI Cards to **dynamic DAX measures** to reflect slicer values
- Connect Power BI directly to FastAPI endpoint for **live scoring**
- Train model incrementally with **streaming/real-time data**
- Integrate with a **case management system** for flagged frauds

---

##  Author

 Built by Rianna Aalto [fuzzyzester](https://github.com/fuzzyzester) –  passionate about end-to-end solutions and real-world insights.

