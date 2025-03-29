
# 💳 Credit Card Fraud Detection – End-to-End ML + Power BI Project

This project presents a **complete fraud detection solution**, combining **machine learning**, **model deployment**, and **interactive Power BI analysis** to identify and monitor fraudulent transactions from a real-world credit card dataset.

>  Fraudulent transactions make up only **0.17%** of the dataset. Handling such **imbalanced data** effectively is the key challenge.

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

The dataset used in this project is a widely referenced **Credit Card Fraud Detection dataset** made publicly available for machine learning research.

It contains **284,807 real credit card transactions** by **European cardholders**, of which only **492 are fraudulent** – making the dataset **highly imbalanced** (~0.17% fraud rate).

###  Data Privacy & Anonymization

Due to the **sensitive nature** of financial data, the original dataset creators anonymized the data to comply with **data protection and privacy regulations**.

####  How?

1. **Personally Identifiable Information (PII)** such as names, locations, and merchant info were removed.
2. A technique called **Principal Component Analysis (PCA)** was applied to transform original features into **anonymized components**, labeled as:
   - `V1` to `V28` → Principal components derived from original transaction details.
   - These preserve patterns in the data while protecting confidentiality.
3. Only **`Time`** and **`Amount`** were kept in their original form:
   - `Time`: Seconds elapsed from the first transaction (later dropped due to low correlation).
   - `Amount`: Transaction value, scaled during preprocessing.

This PCA transformation was performed by the **original data providers** as part of a study published in the research paper:  
> *"Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy"*  
> by **Andrea Dal Pozzolo** et al.

###  What Do “V1” to “V28” Mean?

These are **compressed features** that summarize important transaction behavior. For example:
- `V10`, `V12`, and `V14` show **strong negative correlation** with fraud.
- Others like `V17`, `V18`, and `V4` have weaker signals.

We don’t know the exact original meaning of each — and **that’s by design** — but they still hold **valuable patterns** that our machine learning model can learn from.

---

##  Machine Learning Process

 Check the full code here: [creditcard_fraud.ipynb](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb)

###  Preprocessing
- Dropped irrelevant features (`Time`)
- Scaled `Amount` using `StandardScaler`
- Separated `X` (features) and `y` (target: fraud or not)

###  Model Training & Tuning
Tested multiple models:
- Logistic Regression
- Random Forest (🏆 Best performer)
- XGBoost
- Isolation Forest (for unsupervised detection)

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
  - Pie chart for fraud vs. non-fraud
  - Trend lines for fraud over time
  - Top/Bottom amounts by fraud class
  - Dynamic table of transactions
- Interactive Slicer:
  - Filter by prediction result or amount bracket

> ℹ Note: In the KPI cards, static measures were used. To fully enable dynamic interactivity with slicers, consider converting them to **dynamic measures** using `CALCULATE` + `SELECTEDVALUE`.

---

## 📚 Learnings

- Practical experience in handling real-world **imbalanced data**
- Choosing and tuning ML models with a business impact in mind
- Deploying models for **reusable predictions**
- Communicating results visually through **Power BI**
- Handling **data anonymization** and transforming scaled features

---

##  Future Improvements

- Switch KPI Cards to **dynamic DAX measures** to reflect slicer values
- Connect Power BI directly to FastAPI endpoint for **live scoring**
- Train model incrementally with **streaming/real-time data**
- Experiment with **SMOTE** or **autoencoders** for better fraud recall
- Integrate with a **case management system** for flagged frauds

---

##  Author

 Built by Rianna Aalto [fuzzyzester](https://github.com/fuzzyzester) – Data Scientist & Engineer passionate about end-to-end solutions and real-world insights.

