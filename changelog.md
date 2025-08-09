# 📜 Changelog

All notable changes to this project will be documented in this file.  

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
and adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] – 2025-08-09
### Added
- **Project Introduction** section in `README.md`.
- **Comprehensive EDA** including:
  - Univariate analysis
  - Bivariate analysis
  - Multivariate visualizations
- **Three regression models** implemented:
  - Linear Regression
  - Random Forest Regressor
  - XGBoost Regressor
- **Automatic best model saving** as `best_model.pkl`.
- **Prediction demo** cell that runs with the sample dataset.
- Public demo dataset: `sample_advertising_data.csv`.
- `.gitignore` updates to:
  - Allow sample data
  - Exclude large/real datasets, environment files, and caches.
- **Parameterized notebook** for easy reuse:
  - Dataset paths
  - Target column names
  - Categorical columns
  - Model save paths

### Changed
- Notebook restructured into clear, logical sections:
  1. Project Introduction
  2. Data Loading
  3. Exploratory Data Analysis (EDA)
  4. Preprocessing
  5. Model Training & Evaluation
  6. Best Model Saving
  7. Prediction Demo
- Enhanced markdown explanations and inline code comments.
- Removed duplicate and failed experiment code.

### Fixed
- Resolved encoding issues for categorical columns.
- Fixed feature name mismatches during prediction by ensuring consistent preprocessing between training and new data.

---

## [Unreleased]
### Planned
- Develop a **Streamlit dashboard** for interactive ROAS optimization.
- Add **hyperparameter tuning** for all models.
- Implement **unit tests** for preprocessing and prediction.
- Create **Dockerfile** for containerized deployment.
- Add **CI/CD pipeline** using GitHub Actions for automated testing.
