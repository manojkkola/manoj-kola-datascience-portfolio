# Predicting Stroke Risk Using Machine Learning

## Overview
This capstone project (DSC 680 – Applied Data Science) builds a machine learning pipeline to predict individual stroke risk from patient demographic and clinical data. Stroke accounts for roughly 11% of deaths worldwide, and early identification of at-risk patients can support proactive, preventive care rather than reactive treatment after an event has already occurred.

## Business Problem
How can readily available patient demographic and clinical data be used to predict stroke risk *before* an event occurs, so healthcare providers can move from manual, inconsistent risk stratification toward a validated, data-driven screening tool?

## Dataset
The [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) (Kaggle), containing 5,110 patient records with demographic, lifestyle, and clinical fields (age, hypertension, heart disease, average glucose level, BMI, smoking status, work type, residence type) and a binary stroke outcome. The dataset is heavily imbalanced — 4,861 non-stroke vs. 249 stroke cases (~20:1).

## Approach
1. **Cleaning** — dropped the non-predictive `id` column, imputed 201 missing BMI values with the median, and removed a single `gender = "Other"` record with insufficient representation.
2. **EDA** — visualized class balance, age and glucose distributions by stroke outcome, BMI spread, and a correlation heatmap of numeric features against the target.
3. **Preprocessing** — scaled numeric features with `StandardScaler`, one-hot encoded categorical features, and applied a **stratified 70/30 train-test split** to preserve the class ratio.
4. **Class balancing** — applied **SMOTE** to the training data only, *after* preprocessing, to avoid generating invalid synthetic categorical values and to prevent test-set leakage.
5. **Modeling** — trained and compared four classifiers: Logistic Regression, Decision Tree, Random Forest, and XGBoost, evaluated on accuracy, precision, recall, F1-score, and ROC-AUC.
6. **Interpretation** — extracted Random Forest feature importances to identify and rank the strongest predictors of stroke risk.

## Key Findings
- **Age, average glucose level, hypertension, heart disease, and BMI** emerged as the most significant predictors of stroke risk, consistent with established clinical risk factors.
- **Random Forest achieved the strongest overall accuracy and ROC-AUC**, while **XGBoost achieved the highest recall**, catching more true stroke cases.
- **Logistic Regression had strong recall but low precision**, a direct consequence of the severe class imbalance.
- The Decision Tree model overfit and underperformed relative to the ensemble methods.
- Recall is the most clinically important metric in this context — a missed stroke case is far more costly than a false alarm — but F1-score was used as the primary metric since recall alone can be gamed by an overly aggressive classifier.

## Recommendations
- Use **Random Forest** as the primary model for a clinical decision-support tool, given its balance of accuracy, ROC-AUC, and interpretability.
- Prioritize recall in deployment thresholds to avoid missing high-risk patients, while monitoring the resulting false-positive rate.
- Conduct a **formal fairness audit** across demographic subgroups before any real-world deployment — this was flagged as a limitation rather than fully executed in this project.
- Position the model as a **decision-support signal for clinicians**, not a replacement for medical judgment, with clear HIPAA-compliant governance around its use.

## Limitations
The dataset lacks several clinically important variables (actual blood pressure readings, cholesterol, medication history), the `smoking_status` field has a large "Unknown" category, and the single-source Kaggle dataset may not generalize to broader, more diverse hospital populations.

## Contents
| File | Description |
|---|---|
| `Predicting_Stroke_Risk_Using_Machine_Learning_Milestone_1.docx` | Milestone 1: project proposal and business problem framing |
| `Predicting_Stroke_Risk_Using_Machine_Learning_Milestone_2.docx` | Milestone 2: literature review and methodology plan |
| `Predicting_Stroke_Risk_Using_Machine_Learning.ipynb` / `.pdf` | Full analysis notebook: EDA, preprocessing, modeling, and evaluation |
| `Predicting_Stroke_Risk_Using_Machine_Learning_Final_White_Paper.docx` | Final white paper: business problem, methods, findings, ethics, and recommendations |
| `Predicting_Stroke_Risk_Using_Machine_Learning_Presentation_Script_and_QA.docx` | Presentation script and anticipated audience Q&A |
| `Stroke_Prediction_Presentation.pptx` | Final presentation slides |

## Tools & Methods
Python, pandas, scikit-learn, imbalanced-learn (SMOTE), Logistic Regression, Decision Tree, Random Forest, XGBoost, ROC-AUC/F1 evaluation, feature importance analysis, healthcare analytics ethics

## Author
Manoj Kumar Kola
