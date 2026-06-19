# 08. Machine Learning — Pump it Up: Water Pump Failure Prediction

## 📋 Project Overview
 
This project was developed for the **DrivenData "Pump it Up" competition**, a real-world data science challenge aimed at predicting the functional status of water pumps across Tanzania. The goal is to identify faulty pumps to improve access to clean drinking water in vulnerable communities.
 
**Final Result:** 81.58% accuracy · Ranking #2900 out of ~8,500 submissions

---

## 🎯 Problem Statement
 
The dataset contains over **40 variables** describing water pump characteristics — technical specifications, geographical location, installation details, and usage patterns. The objective is to predict pump status in one of three categories:
 
- `functional` — working properly
- `non functional` — broken, needs replacement
- `functional needs repair` — operational but requires maintenance

This is a **multi-class classification problem** with typical data science challenges: missing values, high-cardinality categorical features, and geographical patterns.
 
---

## 📊 Project Workflow
 
### 1. Exploratory Data Analysis (EDA)
- Visualized missing data patterns
- Analyzed class imbalance and feature distributions
- Identified geographic clustering and feature correlations
- Used `ydata-profiling` for automated data profiling

### 2. Data Preprocessing & Feature Engineering
- **Missing Values:** KNN imputation for numeric features, mode imputation for categorical
- **Outlier Handling:** Winsorizing extreme values in GPS height, population, amount
- **Categorical Encoding:** One-hot encoding for multi-category variables (18+ features)
- **Feature Creation:** Generated pump age (`antiguedad_dias`) from construction year
- **Feature Scaling:** Standardization for tree-based models, normalization alternatives tested

### 3. Handling Class Imbalance
- Applied **SMOTE** oversampling to balance minority classes
- Experimented with class weights in model parameters
- Evaluated impact on precision, recall, and F1-score per class

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

## 📈 Sample Visuals

**Competition Ranking Screenshot**

<img width="551" height="143" alt="image" src="https://github.com/user-attachments/assets/66a34127-ce85-4f40-85a1-f93090dd6770" />

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
  <a href="https://github.com/NicolasSpector">@NicolasSpector</a></i>
</p>
