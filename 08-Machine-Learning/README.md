# 08. Machine Learning — Pump it Up: Water Pump Failure Prediction

## 📋 Overview

End-to-end machine learning project predicting water pump operational status in Tanzania. Built for the **DrivenData "Pump it Up" competition** to identify faulty pumps and restore clean water access.

**Competition Result:** Accuracy **81.58%** · Ranking **#2900** out of ~8,500 submissions

---

## 🤖 Best Model

**Random Forest Classifier**
- n_estimators=200
- Hyperparameter tuning via GridSearchCV
- Class balancing with SMOTE

---

## 📊 Model Comparison

| Model | Accuracy |
|---|---|
| Random Forest | **81.58%** |
| Extra Trees | 80.40% |
| Gradient Boosting | 75.19% |

---

## 🔑 Top Features

1. Quantity (10.7%)
2. Longitude (8.9%)
3. Latitude (8.8%)
4. GPS Height (7.1%)
5. Pump Age (5.7%)

---

## 📈 Sample Visuals

**Competition Ranking Screenshot**

<img width="551" height="143" alt="image" src="https://github.com/user-attachments/assets/66a34127-ce85-4f40-85a1-f93090dd6770" />

---

## 🛠️ Techniques Used

- KNN imputation for missing values
- Winsorizing outliers
- One-hot encoding for categorical variables
- SMOTE for class imbalance
- GridSearchCV hyperparameter tuning

---

## 📁 Files

```
08-Machine-Learning/
├── Nicolas_Esteban_Spector_bombas.ipynb
├── Puntuaciones Competencia.png
└── README.md
```

---

## 📖 View the Notebook

Open `Nicolas_Esteban_Spector_bombas.ipynb` to see the full analysis with all cell outputs, visualizations, and model results.

---

<p align="center">
  <i>Part of <a href="../README.md">Master in Data Science Portfolio</a></i>
</p>
