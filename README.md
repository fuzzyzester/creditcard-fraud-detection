# 💳 Credit Card Fraud Detection & Risk Insights

An end-to-end machine learning and business intelligence project to detect potential fraudulent credit card transactions. This project covers **data preprocessing**, **ML modeling**, **deployment of fraud predictions**, and the creation of a **dynamic Power BI dashboard** to deliver actionable insights to business users and stakeholders.

---

##  Project Objectives

- Identify fraudulent transactions using a supervised ML model
- Create risk scores and confidence levels per transaction
- Allow users to adjust fraud detection sensitivity
- Present model performance and predictions in a clear and intuitive Power BI dashboard
- Align insights with business needs (fraud analysts, finance, risk & HR teams)

---

## 🛠️ Tools & Technologies

| Purpose            | Tools Used                               |
|--------------------|-------------------------------------------|
| Data Preprocessing | Python (Pandas, NumPy, Scikit-learn)      |
| Modeling           | Logistic Regression, Random Forest        |
| Deployment         | Jupyter Notebook, GitHub                  |
| Dashboard & BI     | Power BI Desktop                          |
| Version Control    | Git, GitHub Desktop                       |

---

## 🔄 Workflow Overview

### 1. **Data Exploration & Cleaning**
- Used the Kaggle credit card dataset (anonymized)
- Handled class imbalance using **undersampling** for training
- Scaled transaction amount (StandardScaler)
- Checked correlation and data distribution

### 2. **Feature Engineering**
- Created `Fraud_Probability` output using model.predict_proba
- Engineered:
  - `Risk_Level` (Very Low, Low, Medium, High)
  - `Confidence_Level` (Very High Risk to Very Low Risk)
  - `Prediction_Label` (Fraud / Legitimate)
  - `Actual_Label` (Readable form for ground truth)

### 3. **Modeling**
- Compared Logistic Regression and Random Forest
- Chose Random Forest based on:
  - F1 Score: **0.85**
  - Accuracy: **1.00**
  - Recall: **0.84**
  - Precision: **0.86**

### 4. **Best Practices Followed**
- Used **undersampling** for highly imbalanced binary classification
- Separated feature scaling from label column
- Exported and deployed predictions with interpretable labels
- Used **model evaluation metrics relevant to fraud detection** (Recall & F1 over Accuracy)
- Created readable labels for non-technical users in Power BI

---

##  Power BI Dashboard: Overview

###  Title: **Credit Card Fraud Detection & Risk Insights**

An interactive, clean dashboard to help business stakeholders explore fraud risk in real time.

---

### 🎯 KPI Metrics (Top Row)

| KPI                           | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Total Transactions Checked**  | All transactions reviewed by the system                                     |
| **Flagged as Potential Fraud** | Based on probability threshold slider                                       |
| **Overall Fraud Detection Score** | F1 Score - balance between precision and recall                            |
| **Prediction Accuracy**         | Overall model correctness                                                   |
| **Frauds Successfully Detected** | Recall – proportion of actual frauds caught by the model                   |
| **Correct Fraud Alerts**        | Precision – how many fraud alerts were correct                              |

---

### 🧠 Visuals Explained

#### 📌 **1. Predicted Fraud vs. Non-Fraud (Pie Chart)**
- **Red:** Fraud Prediction  
- **Blue:** Legitimate Prediction  
- Tooltip provides total count and percentage  
- Clear legend with color indicators

#### 📌 **2. Transactions by Fraud Risk Level (Bar Chart)**
- X-axis: Number of transactions
- Y-axis: Fraud probability bins (0.0–0.2, …, 0.8–1.0)
- **Color Legend:**
  - Fraud Prediction = Red
  - Legitimate Prediction = Blue
- Allows comparison of transaction counts by risk bin

#### 📌 **3. Transaction Details Table**
Displays details of each transaction:
- Actual vs Predicted Label
- Confidence Level
- Fraud Probability (as %)
- Risk Level
- Scaled Amount (rounded to 2 decimals)

Users can scroll and filter using the slider to explore data in a business-friendly way.

#### 🎚️ **Dynamic Threshold Slider**
Users can adjust what probability counts as “fraud” (from 0.10 to 0.98), affecting:
- Number of flagged frauds
- All visuals (KPIs, charts, tables)

---

## 🔍 Key Findings

- Model is highly accurate but business users should prioritize **recall** (catching actual frauds)
- **Fraud predictions are rare** (~0.17%), so threshold tuning is critical
- Most legitimate transactions have probabilities below 0.2
- Confidence levels and color-coded risk bins improve interpretability

---

## 📂 Files Included

| File / Folder             | Description                                       |
|---------------------------|---------------------------------------------------|
| `fraud_model.ipynb`       | Python notebook for modeling and exporting output |
| `fraud_predictions.csv`   | Final dataset with predicted labels and scores    |
| `credit_card_fraud.pbix`  | Power BI Dashboard                                |
| `README.md`               | Project documentation                             |
| `assets/`                 | Screenshots, logos, or supporting visuals         |

---

## 🚀 Getting Started

### Prerequisites:
- Power BI Desktop
- Python 3.x with scikit-learn, pandas
- Git/GitHub Desktop

### Clone the repo
```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
