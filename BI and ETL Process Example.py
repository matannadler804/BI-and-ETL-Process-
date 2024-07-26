# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data creation to simulate ETL process
# Creating a mock dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Sales': np.random.randint(100, 500, size=100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
    'Product': np.random.choice(['A', 'B', 'C', 'D'], size=100)
}

# Converting dictionary to DataFrame
df = pd.DataFrame(data)

# ETL Process
# 1. Extract: Loading data into a DataFrame (already done with sample data)
# 2. Transform: Performing data cleaning and transformation
# Adding a new column 'Revenue' calculated as Sales * a random factor
df['Revenue'] = df['Sales'] * np.random.uniform(1.0, 1.5, size=100)

# Handling missing values (if any)
df.fillna(method='ffill', inplace=True)

# 3. Load: Here, we would typically load the data into a data warehouse. For this example, we'll proceed with analysis.

# Data Analysis and Visualization
# Basic statistical summary
print(df.describe())

# Visualization: Sales by Region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=df, palette='viridis')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

# Visualization: Sales over Time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Sales', data=df, marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Visualization: Revenue by Product
plt.figure(figsize=(10, 6))
sns.boxplot(x='Product', y='Revenue', data=df, palette='muted')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()


