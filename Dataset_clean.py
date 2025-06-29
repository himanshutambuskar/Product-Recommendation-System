# dataset_cleaner.py

import pandas as pd

# Load dataset
df = pd.read_csv('dataset/flipkart_com-ecommerce_sample.csv')

# Keep relevant columns only
df = df[['product_name', 'product_category_tree']].dropna()

# Remove unwanted characters from category
df['product_category_tree'] = df['product_category_tree'].str.replace(r"[^\w\s&>]", "", regex=True)

# Combine features
df['combined'] = df['product_name'] + " " + df['product_category_tree']

# Save cleaned dataset
df.to_csv('dataset/cleaned_products.csv', index=False)

print("✅ Cleaned dataset saved.")
