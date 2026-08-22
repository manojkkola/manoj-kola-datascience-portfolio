# Predicting Customer Churn: A Data Mining Approach

## Overview
This project (DSC 550 – Data Mining) analyzes the Telco Customer Churn dataset to identify the key drivers of customer attrition for a telecommunications company. Acquiring new customers costs significantly more than retaining existing ones, so the project frames churn prediction as a direct, actionable business problem: understanding *why* customers leave so at-risk customers can be proactively targeted with retention offers.

## Business Problem
Customer churn is a critical issue for subscription-based telecom providers. The objective is to analyze customer demographics, account details, service subscriptions, and billing data to identify the factors most associated with churn, using the binary `Churn` target column as the outcome of interest.

## Approach
The project was completed across three milestones:
1. **Data Selection & EDA** — loaded the Telco Customer Churn dataset, examined its structure, and produced four graphical analyses of churn against tenure, monthly charges, and contract type.
2. **Data Preparation** — dropped non-informative features (e.g., `customerID`), converted `TotalCharges` to numeric, imputed missing values using `MonthlyCharges`, engineered an `AverageMonthlySpend` feature, encoded the target variable, and one-hot encoded categorical columns.
3. **Modeling & Evaluation** — built and compared a Logistic Regression baseline against a Random Forest model, using accuracy, precision, recall, F1-score, and a confusion matrix, and validated results with 5-fold cross-validation.

## Key Findings
- The dataset is imbalanced, with substantially more non-churning customers than churning ones — an important factor in model evaluation.
- **Customers with shorter tenure churn more**, indicating that early-stage retention is critical.
- **Higher monthly charges are associated with higher churn**, suggesting price sensitivity.
- **Month-to-month contracts churn significantly more** than one-year or two-year contracts.
- Random Forest generally outperformed Logistic Regression on predictive strength, while Logistic Regression offered greater interpretability — highlighting the classic trade-off between model complexity and transparency.

## Contents
| File | Description |
|---|---|
| `Telecommunications_Company_Milestone_1.ipynb` / `.pdf` | Milestone 1: data selection, EDA, and graphical analysis |
| `Telecommunications_Company_Milestone_2.ipynb` / `.pdf` | Milestone 2: data cleaning, transformation, and feature engineering |
| `Telecommunications_Company_Milestone_3.ipynb` / `.pdf` | Milestone 3: model selection, training, and evaluation |
| `Telecommunications_Company_Final_Project.ipynb` | Final combined notebook (all milestones) |
| `Telecommunications_Company_Final_Project.pdf` | Rendered PDF of the final notebook |
| `Telecommunications_Company_Final_Project_Write_Up.docx` | Final written project report |
| `Telco_Customer_Churn.csv` | Source dataset (Kaggle) |

## Tools & Methods
Python, pandas, seaborn/matplotlib, one-hot encoding, MinMax scaling, Logistic Regression, Random Forest, 5-fold cross-validation, confusion matrix analysis

## Author
Manoj Kumar Kola
