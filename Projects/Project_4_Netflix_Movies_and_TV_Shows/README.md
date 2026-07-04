# Exploratory Data Analysis: Netflix Movies and TV Shows

## Overview
This project performs a comprehensive exploratory data analysis (EDA) on a cleaned Netflix content catalog sourced from Kaggle, aiming to uncover patterns in content type, release trends, and metadata relationships. Beyond exploration, the project applies statistical testing, regression, classification, and clustering techniques to turn those patterns into actionable insights for content strategists, data scientists, and business analysts.

## Dataset
The dataset contains metadata for thousands of Netflix titles, including title, type (Movie/TV Show), release year, duration, rating, country, and date added. Missing values in fields like `rating` and `date_added` were addressed through imputation or filtering, and new temporal features (`year_added`, `month_added`) were engineered to support trend analysis.

## Analysis & Methods
- **Univariate analysis**: found that roughly 70% of catalog content is Movies versus 30% TV Shows, with a strong concentration of releases after 2000 and a notable spike between 2016–2020.
- **Bivariate analysis**: a moderate positive correlation between release year and the year content was added to Netflix, suggesting newer content is added more frequently. TV Shows also skew more recent (median release year 2018) than Movies (median 2014).
- **Hypothesis testing**: a two-sample t-test confirmed the difference in release years between Movies and TV Shows is statistically significant (p < 0.05).
- **Regression analysis**: a linear regression model predicting release year from content type produced a modest R² (~0.12) — informative, but not sufficient alone to explain variance in release year.
- **Classification modeling**: a Random Forest classifier predicting content type from release year and duration achieved over 85% accuracy, with release year emerging as the most influential feature.
- **Clustering**: K-Means clustering on a PCA-reduced feature set was used to explore unsupervised structure in the data, with the optimal cluster count determined via the elbow method.

## Key Findings
- Content type distribution and release timing show clear, statistically significant patterns rather than random variation.
- Release year and duration alone can predict content type (Movie vs. TV Show) with high accuracy, suggesting potential utility for automated tagging or recommendation systems.
- Simple regression is a poor fit for release-year prediction — more complex or non-linear approaches would likely perform better.

## Contents
| File | Description |
|---|---|
| `Netflix_Movies_and_TV_Shows_Code.ipynb` | Jupyter notebook with data cleaning, EDA, hypothesis testing, and modeling code |
| `Netflix_Movies_and_TV_Shows_Code.pdf` | Rendered PDF of the analysis notebook |
| `Netflix_Movies_and_TV_Shows_Project_Narrative.pdf` | Final project narrative and write-up of findings |

## Tools & Methods
Python, pandas, Exploratory Data Analysis, hypothesis testing, linear regression, Random Forest classification, K-Means clustering, PCA

## Author
Manoj Kumar Kola
