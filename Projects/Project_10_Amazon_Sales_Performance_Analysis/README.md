# Amazon Sales Performance Analysis: Identifying Factors That Influence Revenue

## Overview
This capstone project (DSC 680 – Applied Data Science) analyzes a five-year Amazon-style transaction dataset to test which factors are genuinely associated with high-performing sales orders. Rather than simply reporting totals by category or region, the project builds a rigorous predictive framework — including an explicit leakage-prevention design and a diagnostic ablation study — to determine whether business-reported dimensions carry real predictive signal or are simply noise.

## Business Problem
Which product-, sales-, and customer-related factors are associated with higher sales performance in Amazon transactional data — and can non-transactional factors alone (category, region, payment method, timing, salesperson) reliably distinguish high-performing orders from lower-performing ones?

## Dataset
The [Amazon Sales Dataset for Performance Analysis](https://www.kaggle.com/datasets/rahuljangir78/amazon-sales-dataset-for-performance-analysis) (Kaggle), containing 5,000 orders from January 2019 through December 2024 across 7 product categories and 5 global regions, with fields covering order details, salesperson, payment method, order status, and financial outcomes.

## Approach
1. **Cleaning & verification** — filled one missing `Product Name` with "Unknown," recalculated `Total Sales` from `Quantity Sold × Unit Price × (1 − Discount%)` to confirm data integrity, and extracted `Order Year`, `Order Month`, `Order Quarter`, and `Order Day of Week` from `Order Date`.
2. **Target definition** — created a binary **`High Sales`** indicator via a median split on `Total Sales`, producing two naturally balanced classes rather than relying on an arbitrary threshold.
3. **Leakage prevention** — deliberately excluded `Quantity Sold`, `Unit Price`, `Discount (%)`, and `Profit Margin` from the model's input features, since these fields mathematically determine `Total Sales` and would let the model "cheat" instead of learning genuine business patterns.
4. **Modeling** — trained and compared Logistic Regression, Decision Tree, Random Forest, and XGBoost on the remaining non-transactional features (category, region, payment method, order status, salesperson, timing), with SMOTE applied for consistency.
5. **Diagnostic ablation study** — directly tested reviewer feedback by (a) confirming the SMOTE-resampled training set was already perfectly balanced (1,750/1,750) and had zero measurable effect on results, and (b) reintroducing the excluded transaction-size fields into a benchmark model purely to quantify how much predictive ceiling their exclusion gives up.

## Key Findings
- **All four models performed close to random chance** (ROC-AUC between 0.48 and 0.52) when restricted to non-transactional features — category, region, payment method, salesperson, and timing carry almost no signal about whether an order will be high- or low-value.
- **Reintroducing transaction-size fields (quantity, price, discount) lifted ROC-AUC to 0.977–0.9995** — near-perfect separation — confirming that order value is almost entirely a function of transaction size, not of who, where, or when the purchase occurred.
- **SMOTE had zero measurable effect**: the median-split target was already exactly balanced before resampling, so its inclusion was retained only for methodological transparency.
- Sales were fairly evenly distributed across product categories (Sports, Clothing, and Toys led; Beauty trailed by only ~11%) and regions (South America led, North America lowest), with no single dimension dominating.

## Why a "Null Result" Is the Finding
This project's central conclusion isn't which category or region wins — it's that, within this dataset, none of the commonly reported business dimensions can reliably predict order value on their own. That's a genuinely useful, actionable result: it tells category managers and regional leaders not to over-invest in segmentation models built on these attributes, and instead to focus forecasting effort on the variables that actually drive revenue — order size and pricing.

## Contents
| File | Description |
|---|---|
| `Project_10_Amazon_Sales_Performance_Analysis_Milestone_1.docx` | Milestone 1: proposal and business problem framing |
| `Project_10_Amazon_Sales_Performance_Analysis_Milestone_2.docx` | Milestone 2: methodology and initial modeling plan |
| `Project_10_Amazon_Sales_Performance_Analysis.ipynb` | Full analysis notebook: EDA, feature engineering, modeling, and the diagnostic ablation study |
| `Project_10_Amazon_Sales_Performance_Analysis_Final_White_Paper.docx` | Final white paper: business problem, methods, findings, and recommendations |
| `Project_10_Amazon_Sales_Performance_Analysis.pptx` | Final presentation slides |
| `amazon_sales_dataset_2019_2024_corrected.xlsx` | Source dataset (Kaggle) |

## Tools & Methods
Python, pandas, scikit-learn, imbalanced-learn (SMOTE), Logistic Regression, Decision Tree, Random Forest, XGBoost, data leakage prevention, ablation testing, ROC-AUC evaluation, feature importance analysis

## Author
Manoj Kumar Kola
