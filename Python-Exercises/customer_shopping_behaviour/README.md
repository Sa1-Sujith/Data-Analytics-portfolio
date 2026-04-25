# Customer Shopping Behavior: Advanced EDA & Feature Engineering

## Overview
This repository contains a Python-based data preparation pipeline utilizing Pandas. The script cleans a retail dataset of 3,900 customer transactions, handles missing values, and engineers complex behavioral features to ready the data for business intelligence and predictive modeling.

## Key Pipeline Steps
1. **Standardization & Imputation**: 
   - Standardized column headers to snake_case.
   - Contextually imputed missing `review_rating` values using category-specific medians.
2. **Redundancy Elimination**: 
   - Identified a 100% correlation between `discount_applied` and `promo_code_used`. Dropped the redundant `promo_code_used` column to reduce dimensionality.
3. **Demographic Segmentation**: 
   - Discretized continuous `age` data into statistically balanced quantiles (`Young Adult`, `Adult`, `Middle Age`, `Senior`).
4. **Behavioral & Financial Modeling**: 
   - Mapped qualitative strings (e.g., 'Fortnightly') to numerical timeframes (`purchase_frequency_days`).
   - Derived a new `estimated_annual_spend` metric using purchase frequency and average transaction size to identify high-lifetime-value customers.

## Technologies Used
* **Python**
* **Pandas** (Data wrangling, imputation, feature engineering)
