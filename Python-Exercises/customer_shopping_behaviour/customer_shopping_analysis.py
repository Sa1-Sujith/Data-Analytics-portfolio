# DATA LOADING & SETUP
import pandas as pd

# Load the dataset
df = pd.read_csv("customer_shopping_behavior.csv")


# DATA CLEANING & IMPUTATION

# Impute missing review ratings based on the median of their respective category
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


#COLUMN STANDARDIZATION & REDUNDANCY CHECK

# Standardize column names to snake_case
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# Drop redundant column (discount_applied and promo_code_used are identical)
df = df.drop('promo_code_used', axis=1)

# FEATURE ENGINEERING (DEMOGRAPHICS)
# Segment ages into balanced quantiles
labels = ['Young Adult', 'Adult', 'Middle Age', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# FEATURE ENGINEERING (BEHAVIORAL & FINANCIAL)
# Map text-based frequencies to numerical days
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# Calculate estimated annual spend per customer
df['estimated_annual_spend'] = (365 / df['purchase_frequency_days']) * df['purchase_amount']


# FINAL DATA VALIDATION

print("--- Final Dataset Info ---")
print(df.info())
print("\n--- Preview of Engineered Features ---")
print(df[['customer_id', 'age_group', 'purchase_frequency_days', 'estimated_annual_spend']].head())
