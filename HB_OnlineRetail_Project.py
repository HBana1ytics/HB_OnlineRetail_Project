#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project: Online Retail Exploratory Data Analysis with Python

# ## Overview
# 
# In this project, you will step into the shoes of an entry-level data analyst at an online retail company, helping interpret real-world data to help make a key business decision.

# ## Case Study
# In this project, you will be working with transactional data from an online retail store. The dataset contains information about customer purchases, including product details, quantities, prices, and timestamps. Your task is to explore and analyze this dataset to gain insights into the store's sales trends, customer behavior, and popular products. 
# 
# By conducting exploratory data analysis, you will identify patterns, outliers, and correlations in the data, allowing you to make data-driven decisions and recommendations to optimize the store's operations and improve customer satisfaction. Through visualizations and statistical analysis, you will uncover key trends, such as the busiest sales months, best-selling products, and the store's most valuable customers. Ultimately, this project aims to provide actionable insights that can drive strategic business decisions and enhance the store's overall performance in the competitive online retail market.
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and Pandas. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - numpy
# - seaborn
# - matplotlib
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`

# ## Project Objectives
# 1. Describe data to answer key questions to uncover insights
# 2. Gain valuable insights that will help improve online retail performance
# 3. Provide analytic insights and data-driven recommendations

# ## Dataset
# 
# The dataset you will be working with is the "Online Retail" dataset. It contains transactional data of an online retail store from 2010 to 2011. The dataset is available as a .xlsx file named `Online Retail.xlsx`. This data file is already included in the Coursera Jupyter Notebook environment, however if you are working off-platform it can also be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
# 
# The dataset contains the following columns:
# 
# - InvoiceNo: Invoice number of the transaction
# - StockCode: Unique code of the product
# - Description: Description of the product
# - Quantity: Quantity of the product in the transaction
# - InvoiceDate: Date and time of the transaction
# - UnitPrice: Unit price of the product
# - CustomerID: Unique identifier of the customer
# - Country: Country where the transaction occurred

# ## Tasks
# 
# You may explore this dataset in any way you would like - however if you'd like some help getting started, here are a few ideas:
# 
# 1. Load the dataset into a Pandas DataFrame and display the first few rows to get an overview of the data.
# 2. Perform data cleaning by handling missing values, if any, and removing any redundant or unnecessary columns.
# 3. Explore the basic statistics of the dataset, including measures of central tendency and dispersion.
# 4. Perform data visualization to gain insights into the dataset. Generate appropriate plots, such as histograms, scatter plots, or bar plots, to visualize different aspects of the data.
# 5. Analyze the sales trends over time. Identify the busiest months and days of the week in terms of sales.
# 6. Explore the top-selling products and countries based on the quantity sold.
# 7. Identify any outliers or anomalies in the dataset and discuss their potential impact on the analysis.
# 8. Draw conclusions and summarize your findings from the exploratory data analysis.

# ## Task 1: Load the Data

# In[28]:


pip install pandas  


# In[29]:


import pandas as pd 


# In[30]:


import numpy as np 


# In[31]:


pip install pandas openpyxl pyodbc 


# In[32]:


df = pd.read_excel(r"Online Retail.xlsx", engine='openpyxl')  


# In[33]:


df.head()  


# In[34]:


print(df.shape)  


# In[35]:


df.info()  


# In[36]:


print(df.isnull().sum())  


# In[37]:


print(df.dtypes)  


# In[38]:


df.drop_duplicates(inplace=True)  


# In[39]:


df = df.dropna()  


# In[40]:


print(df.shape)  


# In[41]:


df['CustomerID'] = pd.Series(df['CustomerID'], dtype="string") 


# In[42]:


print(df.dtypes)  


# In[43]:


# Total Sales per transaction   
df['TotalSales'] = df['Quantity'] * df['UnitPrice']  


# In[44]:


# Extract Month and Day from InvoiceDate   
df['Month'] = df['InvoiceDate'].dt.month
df['Weekday'] = df['InvoiceDate'].dt.day_name()  


# In[45]:


df.head()  


# In[46]:


df.describe()  


# In[47]:


import matplotlib.pyplot as plt  
import seaborn as sns  


# # 1. Sales Trends Over Time  
# a. Monthly sales  b. Sales by day of week or Weekday  

# In[48]:


import pandas as pd
import matplotlib.pyplot as plt 

# Set the date as index and resample monthly
monthly_sales = df.set_index('InvoiceDate').resample('M')['TotalSales'].sum()

# Plotting the trend
plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title('Monthly_Sales_Trend')
plt.ylabel("TotalSales")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()
plt.show()


# In[49]:


weekday_sales = df.groupby('Weekday')['TotalSales'].sum().reindex(
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

weekday_sales.plot(kind='bar', title='Sales_by_Day_of_the_Week')  


# In[50]:


saturday_sales = df[df['Weekday'] == 'Saturday']

# Check if there are any sales on Saturday
if saturday_sales.empty:
    print("No sales on Saturday.")
else:
    print(f"Number of Saturday transactions: {len(saturday_sales)}")
    print(f"Total Saturday Sales: {saturday_sales['Sales'].sum()}")


# # 2. Top Product   

# In[51]:


top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10) 
top_products.plot(kind='barh', title='Top-Selling Products', figsize=(10,6))  


# 
# # 3. Sales by Country   

# In[52]:


country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(10) 
country_sales.plot(kind='bar', title='Top_Countries_by_Sales', figsize=(10,6))  


# # 4. Outliers & Anomalies, Spot unusual transactions   

# In[53]:


sns.boxplot(x=df['TotalSales']) 
plt.title('Transaction Value Distribution')   


# 
# # 5. Key Customer Analysis   

# In[54]:


customer_sales = df.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False).head(10) 
customer_sales.plot(kind='bar', title='Top_10_Customers_by_Value')  


# # Key Questions and their Answers and Insights. 
# 
# Which months has the most sales? Are there any seasonal patterns?   
# : October, November and December have the peak, probably due to holiday season 
# 
# Which products sell the most? 
# : WORLD WAR 2 GLIDERS ASSTD DESIGNS, JUMBRO BAG RED RETROSPOT, POPCORN HOLDER 
# 
# Who are the top customers? 
# : customerID 14646.0 , 18102.0  
# 
# Which countries generate most revenue?  
# : UK dominates, followed by Netherlands, EIRE.    

# # Recommendations   
# 
# 1. Promotions during peak months 
# 2. Focus marketing on high-selling products 
# 3. Build loyalty with top customers. 
# 

#  

# In[ ]:





# In[ ]:





# In[ ]:




