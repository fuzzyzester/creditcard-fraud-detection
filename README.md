#  Credit Card Fraud Detection (with FastAPI Deployment + Power BI Dashboard)

This project aims to **detect fraudulent credit card transactions** using machine learning, deploy the best model via **FastAPI**, and visualize insights and prediction results in **Power BI**.

<br>

![Power BI Dashboard](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png)

🔗 [Power BI Dashboard (Full View)](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png)

---

##  Table of Contents

- [ Dataset](#dataset)
- [ Data Preprocessing](#data-preprocessing)
- [ Handling Class Imbalance](#handling-class-imbalance)
- [ Model Building & Evaluation](#model-building--evaluation)
- [ Overfitting/Underfitting Analysis](#overfittingunderfitting-check)
- [ Final Model Selection](#final-model-selection)
- [ FastAPI Deployment](#fastapi-deployment)
- [ Power BI Integration](#power-bi-integration)
- [ Learnings](#learnings)
- [ Future Improvements](#future-improvements)
- [ Project Links](#project-links)
- [ Author](#author)

---

##  Dataset

- **Source**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Rows**: 284,807 transactions
- **Fraud cases**: 492 (~0.17%)
- Features: V1–V28 (PCA-transformed), `Amount`, `Time`, `Class` (target)

---

##  Data Preprocessing

1. Dropped `Time` (not useful for prediction).
2. Scaled the `Amount` column using `StandardScaler`.
3. Renamed it to `Scaled_Amount` and moved `Class` to the end.
4. Final dataset: `X` (features), `y` (target)

 [View Full Notebook](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb)

---

##  Handling Class Imbalance

Instead of using SMOTE, this project handled imbalance **within the model**:

- `class_weight='balanced'` for Logistic Regression & Random Forest
- `scale_pos_weight = (count_0 / count_1)` for XGBoost

✅ Avoids synthetic data and works well for real-time APIs.

---

##  Model Building & Evaluation

Trained and evaluated:

1. **Logistic Regression**
2. **Random Forest (Tuned)**
3. **XGBoost**

### Metrics Used:

- Precision
- Recall
- F1-Score
- ROC-AUC

###  Evaluation Table:

| Model               | Precision (1) | Recall (1) | F1-score (1) | ROC-AUC |
|--------------------|---------------|------------|--------------|---------|
| Logistic Regression| 0.056         | 0.918      | 0.106        | 0.970   |
| Random Forest       | 0.943         | 0.847      | 0.892        | 0.958   |
| XGBoost             | 0.685         | 0.867      | 0.766        | 0.975   |

---

##  Overfitting/Underfitting Check

```
Random Forest:
Train F1 (1): 1.000 | Test F1 (1): 0.892 → Overfitting

Tuned RF (Final):
Train F1 (1): 0.937 | Test F1 (1): 0.818 →  Acceptable

Logistic Regression:
Stable, no overfitting. Low precision though.
```

---

##  Final Model Selection

**✔ Selected:** Tuned **Random Forest Classifier**

- Good trade-off between precision and recall
- ROC-AUC: 0.984 on test
- Slight overfitting, but improved with tuning

 [Download Final Model (.pkl)](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_model_final.pkl)

 [Predictions CSV](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_predictions.csv)

---

##  FastAPI Deployment

The final model was deployed using **FastAPI**, making predictions available via RESTful API.

### ▶ Example Prediction Request

```json
POST /predict

{
  "V1": -1.3598,
  "V2": -0.0728,
  ...
  "V28": -0.0210,
  "Scaled_Amount": 0.244
}
```

###  Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0023
}
```

 Run locally with:

```bash
uvicorn main:app --reload
```

---

##  Power BI Integration

- Power BI connected to the API or processed `.csv`
- Visualized:
  - Predictions
  - Fraud vs. non-fraud counts
  - Probability scores
- Interactive filters by predicted class

 [Dashboard Screenshot](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png)

---

## 📚 Learnings

-  Model balancing strategies without SMOTE
-  Model tuning and evaluation with class imbalance
-  Deployed a real ML model with FastAPI
-  Embedded ML insights into Power BI for business use
-  Applied ROC-AUC and F1 in real-world imbalanced cases

---

## 🛠 Future Improvements

-  Cloud-host the FastAPI (Azure, Railway, Render)
-  Add auth/security to API endpoint
-  Try stacking or ensemble learning
-  Add batch-upload prediction route
-  Add anomaly scoring with dynamic thresholds in Power BI

---

## 📁 Project Links

-  Notebook: [creditcard_fraud.ipynb](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/creditcard_fraud.ipynb)  
-  Final Model: [fraud_model_final.pkl](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_model_final.pkl)  
-  Predictions: [fraud_predictions.csv](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/fraud_predictions.csv)  
-  Power BI Dashboard: [Screenshot](https://github.com/fuzzyzester/creditcard-fraud-detection/blob/main/powerBIdashboard_CreditCard_fraud_detection.png)

---

##  Author

 Built and deployed by **[fuzzyzester](https://github.com/fuzzyzester)**  
 Aspiring Data Scientist & Data Engineer | Passionate about real-world ML solutions

---
