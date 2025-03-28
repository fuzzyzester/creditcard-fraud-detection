
# 💳 Credit Card Fraud Detection & Risk Insights

This project showcases an end-to-end machine learning solution for detecting credit card fraud, deploying the model via FastAPI, and visualizing key results and KPIs through a compelling Power BI dashboard. It blends both **Data Science** and **Data Engineering** best practices.

---

##  Objective

- Detect fraudulent transactions using ML models.
- Deploy the model via a FastAPI REST API.
- Create a business-facing interactive Power BI dashboard.
- Demonstrate the ML lifecycle including data preparation, modeling, evaluation, deployment, and visualization.

---

##  Machine Learning Process

### 1️⃣ Exploratory Data Analysis (EDA)

- **Time** was dropped as it had no predictive value.
- **V1–V28**: PCA-transformed features.
- **Amount**: Skewed and required scaling.
- **Class**: Highly imbalanced (0 = Legit, 1 = Fraud).

### 2️⃣ Missing and Duplicates Check
- No missing values found.
- Duplicate transactions were removed for model clarity.

### 3️⃣ Class Imbalance Check
- 99.83% legitimate vs 0.17% fraud.
- Addressed using class weighting and stratified sampling.

### 4️⃣ Distribution and Outlier Analysis
- Amount had outliers and was heavily right-skewed.
- Scaled using `StandardScaler` → `Scaled_Amount`.

### 5️⃣ Correlation Analysis
- V10, V12, V14 were highly correlated with the fraud class.
- Features like `Time` were removed.

---

## 🔧 Data Preprocessing

- Scaled `Amount` column.
- Dropped uninformative columns.
- Final dataset: 28 PCA features + Scaled_Amount + Class.

---

## 🤖 Model Training

### Models Compared:
| Model              | Precision | Recall | F1 Score | AUC   |
|-------------------|-----------|--------|----------|--------|
| Logistic Regression | 0.8289   | 0.6429 | 0.7241   | 0.9560 |
| Random Forest       | 0.9419   | 0.8265 | 0.8804   | 0.9528 |
| XGBoost             | 0.8632   | 0.8367 | 0.8497   | 0.9695 |

### Best Model: ✅ Tuned XGBoost
- Achieved **F1: 0.8497**, **AUC: 0.9723** after tuning with `RandomizedSearchCV`.

---

##  Model Deployment (FastAPI)

The trained model was deployed using a RESTful API via **FastAPI**.

### Features:
- Endpoint `/predict` accepts JSON input of transaction features.
- Returns prediction (Fraud/Legitimate) and confidence score.
- Built using `Pydantic` for schema validation.
- Docker-ready and production-scalable.
- Model and scaler saved using `joblib`.

---

## 📤 Data Engineering Practices

- **Model Serialization**: `joblib.dump()` to save models.
- **FastAPI Deployment**: Clean routing, schema validation.
- **Prediction Pipeline**: API returns both class and fraud probability.
- **Automated CSV Export**: Predictions saved as `fraud_predictions.csv` for Power BI.
- **Modular Structure**: Data pipeline separated from ML code.

---

##  Power BI Dashboard Highlights

![Dashboard Preview](./Screenshot_2025-03-28_125428.png)

### Key Sections:
- **KPIs**: Total Transactions, Accuracy, Precision, Recall, F1, Detection Score.
- **Charts**: Fraud Distribution Pie, Prediction Confidence Bar.
- **Table**: Transaction drill-down with fraud probability, actual & predicted labels.
- **Dynamic Filtering**: Slider for threshold, dropdowns for class & confidence.

### Enhanced UX Features:
- Soft shadows and white backgrounds.
- Rounded corners on cards.
- Clear legend labels (Fraud Prediction, Legitimate Prediction).
- Tooltip explanations for confidence, scaled amount, and risk score.

---

##  Project Structure

```
credit-card-fraud-detection/
├── data/
├── notebooks/
├── api/
│   ├── main.py
│   └── schemas.py
├── models/
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── xgboost_model_pre_tuned.pkl
│   └── tuned_xgboost_model.pkl
├── exports/
│   └── fraud_predictions.csv
├── powerbi/
│   └── Fraud_Dashboard.pbix
└── README.md
```

---

## 🔍 Key Learnings

- Working with real-world imbalanced datasets requires careful evaluation metrics.
- XGBoost is a strong performer for fraud use cases.
- FastAPI is a lightweight yet powerful option for model deployment.
- Power BI can turn complex ML outputs into business-friendly visuals.

---

##  Future Improvements

- Integrate real-time fraud detection (streaming).
- Add SHAP interpretability for feature importance.
- Automate with Data Factory or Airflow.
- CI/CD for model updates and dashboard refresh.

---

##  Final Note

This project bridges **Data Science**, **Data Engineering**, and **Business Intelligence** to deliver real-world, production-ready fraud detection and insights.

---

 
**Tools Used**: Python, scikit-learn, XGBoost, FastAPI, Power BI, GitHub  
**Dataset**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
