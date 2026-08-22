# Predicting Customer Churn: A Predictive Analytics Pipeline

## Overview
This project (DSC 630 – Predictive Analytics) builds on the churn analysis work from Project 6, expanding it into a full predictive analytics pipeline using the same Telco Customer Churn dataset. Where Project 6 focused on data mining fundamentals, this project emphasizes end-to-end model benchmarking, class-imbalance handling, hyperparameter tuning, and business-oriented interpretation aimed at driving concrete retention recommendations.

## Dataset
The Telco Customer Churn dataset (7,043 customers, ~26.6% churn rate) with demographic, account, billing, and service-subscription fields. `TotalCharges` was converted to numeric and 11 missing values were imputed with the column median.

## Approach
1. **EDA** — examined churn distribution, contract type, monthly charges, tenure, and internet service type against churn, plus correlation heatmaps of encoded features.
2. **Preprocessing** — label-encoded categorical features, split data into train/test sets, applied **SMOTE** to the training set only (to avoid data leakage) to correct the ~74/26 class imbalance, and scaled features with `StandardScaler`.
3. **Modeling** — trained and compared four classifiers: Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting, evaluated via accuracy, F1-score, and ROC-AUC.
4. **Tuning** — used `GridSearchCV` to tune the best-performing Gradient Boosting model across `n_estimators`, `learning_rate`, `max_depth`, and `min_samples_split`, and validated stability with 5-fold cross-validation.
5. **Interpretation** — analyzed feature importances, confusion matrices, precision-recall trade-offs, and error patterns (false negatives vs. false positives) to translate model output into business recommendations.

## Key Findings
- **Baseline Gradient Boosting achieved the best ROC-AUC (0.8214)** on the held-out test set of 1,407 customers; the tuned model landed at a balanced operating point (AUC 0.8169, 60% churn recall, 55% precision).
- **Logistic Regression delivered the highest churn recall (72%)**, making it the strongest single-metric performer on the most business-critical metric — catching actual churners.
- **`Contract` type is by far the dominant churn driver**, accounting for ~40% of the Gradient Boosting model's feature importance — far outweighing `MonthlyCharges` (12%) and `TotalCharges` (11%).
- Service add-ons like `OnlineSecurity` and `TechSupport` are protective: their absence correlates with higher churn.
- The model correctly identifies 226 of 374 actual churners (60.4%) in the test set, while 148 churners remain undetected — the model's practical improvement ceiling given current features.

## Business Recommendations
1. **Prioritize contract migration** — actively convert month-to-month customers to annual contracts through rate-lock or loyalty incentives, since contract type is the single largest churn signal.
2. **Run value reviews for high-charge customers** — proactively audit accounts above the median monthly charge who lack an annual contract.
3. **Deploy the model as a monthly churn-risk scoring engine**, flagging the top 20% highest-risk customers for retention outreach.
4. **Bundle OnlineSecurity/TechSupport into onboarding** as opt-out trials to increase product stickiness.
5. **Investigate fiber-optic churn specifically** — fiber customers churn more than DSL despite being a premium tier, warranting qualitative follow-up (NPS surveys, support ticket review).

## Contents
| File | Description |
|---|---|
| `DSC630_Manoj_Kola_Term_Project_Milestone_3.ipynb` / `.pdf` | Milestone 3: EDA, cleaning, and initial model benchmarking |
| `DSC630_Manoj_Kola__Project_Milestone_2.docx` | Milestone 2: written project narrative |
| `DSC630_Manoj_Kola_Term_Project_Milestone_4.ipynb` / `.pdf` | Milestone 4: hyperparameter tuning and advanced evaluation |
| `DSC630_Manoj_Kola_Final_Project_Milestone_5.ipynb` / `.pdf` | Final notebook: full modeling pipeline, interpretation, and recommendations |
| `DSC630_Manoj_Kola_Final_Paper.docx` | Final written report |
| `DSC630_Manoj_Kola_Final_Presentation.pptx` | Final presentation slides |
| `Telco_Customer_Churn.csv` | Source dataset (Kaggle) |

## Tools & Methods
Python, pandas, scikit-learn, imbalanced-learn (SMOTE), Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, GridSearchCV, ROC-AUC/precision-recall analysis, feature importance interpretation

## Author
Manoj Kumar Kola
