import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

df=pd.read_csv("E:/Github Repositories/Future-interns-intership/FUTURE_DS_02/cleaned2_data.csv")

# Bussiness question 

# Churn rates & retention trends
# CHURN RATES
total_customer=len(df)
churn_customer=df[df['Churn']=='YES'].shape[0]
churn_rates=(churn_customer/total_customer)*100
print(churn_rates)

# # retention 
# total_customer=len(df)
# retention_customer=df[df['Churn']=='NO'].shape[0]
# retention_customer=(retention_customer/total_customer)*100
# print(retention_customer)

#  retention_trends
# retention_trends=df.groupby('tenure')['Churn'].value_counts(normalize=True).unstack()
# print(retention_trends)


# Contract-based Cohort

# contract_based=df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
# print(contract_based)

# PaymentMethod
# PaymentMethod=df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
# print(PaymentMethod)

# InternetService
# InternetService=df.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack()
# print(InternetService)

# customer-lifetime
# avg_life=df['tenure'].mean()
# print(avg_life)

# drop_analysis=df.groupby('tenure')['Churn'].value_counts(normalize=True).unstack()
# print(drop_analysis)