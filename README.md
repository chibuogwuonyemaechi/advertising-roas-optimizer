---
title: Advertising Campaign ROAS Optimizer
emoji: 📊
colorFrom: yellow
colorTo: blue
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
license: mit
tags:
  - machine-learning
  - marketing
  - advertising
  - streamlit
  - data-science
---

# 📊 Advertising Campaign ROAS Optimizer
[![GitHub release](https://img.shields.io/github/v/release/chibuogwuonyemaechi/advertising-roas-optimizer?color=blue&label=Release)](https://github.com/chibuogwuonyemaechi/advertising-roas-optimizer/releases/tag/v1.0)

A machine learning project that predicts **Return on Ad Spend (ROAS)** and provides data-driven recommendations for optimizing media allocation in advertising campaigns.  
Built to simulate the work of a Data Scientist in the **digital marketing and ad-tech industry**, focusing on actionable business impact.

---

## 📢 Release Notes – v1.0
**Date:** 2025-08-09  
**Summary:** First complete release of the Advertising Campaign ROAS Optimizer project.

### Changes:
- Added full EDA section with univariate, bivariate, and multivariate analysis.
- Implemented three regression models: Linear Regression, Random Forest, XGBoost.
- Added automatic best model saving (`best_model.pkl`).
- Included prediction demo that runs with a sample dataset.
- Created `sample_advertising_data.csv` for GitHub demo usage.
- Updated `.gitignore` to allow sample data and exclude large/real datasets.
- Polished README.md with professional project structure and usage guide.

---

## 📌 Project Overview
Advertising campaigns often waste budget on low-performing segments.  
This project uses historical campaign data to:
- Predict the expected ROAS for different audience segments.
- Recommend optimized budget allocations.
- Simulate the impact of these changes using **A/B testing**.

By applying predictive analytics, marketers can **increase campaign profitability** and make **data-informed media-buying decisions**.

---

## 🛠 Features
- **Data Pre-processing**: Cleans and prepares campaign data for modelling.
- **Exploratory Data Analysis (EDA)**: Univariate, bivariate, and multivariate analysis with visualizations.
- **Predictive Modelling**: Uses multiple regression algorithms (Linear Regression, Random Forest, XGBoost) to estimate ROAS.
- **Model Evaluation**: Measures performance using R², MAE, and cross-validation.
- **Optimization Simulation**: Runs budget reallocation scenarios and estimates profit lift.
- **Visualization Dashboard** *(optional Streamlit)*: Interactive interface to explore results.
- **Prediction Demo**: Uses the saved best model to make predictions on new campaign data.

---

## 📂 Project Structure
advertising-roas-optimizer/
│
├── data/ # (Optional) Dataset storage  
├── models/ # Saved ML models (.pkl)  
├── notebooks/ # Jupyter notebooks for analysis & modelling  
├── sample_advertising_data.csv # Sample dataset for demo  
├── requirements.txt # Python dependencies  
├── .gitignore # Ignored files & folders  
├── README.md # Project documentation  
└── CHANGELOG.md # Release history  

---

## 🧰 Tech Stack
- **Language**: Python 3.x
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn, Joblib
- **Visualization**: Power BI / Streamlit
- **Version Control**: Git, GitHub, Hugging Face
- **Environment**: Jupyter Notebook

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/chibuogwuonyemaechi/advertising-roas-optimizer.git
   cd advertising-roas-optimizer
