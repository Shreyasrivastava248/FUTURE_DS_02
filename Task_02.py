import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing data set

df=pd.read_csv('E:/Github Repositories/Future-interns-intership/FUTURE_DS_02/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)
# check 5 row
print(df.head())
print(df.shape)
print(df.describe)

# check null value
print(df.isnull().sum())
# there is no null value 
# check duplicate
df = df.drop_duplicates(subset=['customerID'], keep='first')
print(df['customerID'].duplicated().sum())
print(df['customerID'].nunique())
# check datatype
print(df.dtypes)
df['SeniorCitizen']=df['SeniorCitizen'].map({0:'no',1:'yes'})
print(df['SeniorCitizen'])
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
print(df['TotalCharges'])
# trim and regx

cols=['customerID','gender','SeniorCitizen',	'Partner',	'Dependents',	'PhoneService',	'MultipleLines'	,'InternetService',	'OnlineSecurity',	'OnlineBackup',	'DeviceProtection','TechSupport',	'StreamingTV',	'StreamingMovies',	'Contract',	'PaperlessBilling',	'PaymentMethod','Churn']
df[cols] = df[cols].apply(lambda x: x.str.strip().str.upper())
print(df[cols])

df['Churn_Flag']=df['Churn'].map({'YES':1,'NO':0})
# save the clean file
df.to_csv("E:/Github Repositories/Future-interns-intership/FUTURE_DS_02/cleaned2_data.csv",index=False)
print("updated file is save")

