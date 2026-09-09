import pandas as pd
import numpy as np
df = pd.read_csv('../data/default_creditrisk.csv')

print(df.head()) ## uppar ka 5 rows print krke dikaye ga 

print(df.shape) ## (rows,columns) bataye ga 

print(df.info()) ## sare columns ke across not-null count dega , datatype dega 

print(df.isnull().sum()) ## har columns ke across sum of null value in that column dega 

print(df.describe()) ## ye sara cheej bata dega count of rows , mean, min , max , ...... in each column

df["credit_utilization"] = (
    df["BILL_AMT1"] /
    df["LIMIT_BAL"])
print(df[["LIMIT_BAL","BILL_AMT1","credit_utilization"]].head())  ## naya column banaye hh credit utilization krke 

df["payment_ratio"] = np.where(
    df["BILL_AMT1"] > 0,
    df["PAY_AMT1"] /
    df["BILL_AMT1"],
    np.nan)
print(df[["PAY_AMT1","BILL_AMT1","payment_ratio"]].head())  ## yaha bhi naya column payment_ratio bana  

bill_cols = [
'BILL_AMT1',
'BILL_AMT2',
'BILL_AMT3',
'BILL_AMT4',
'BILL_AMT5',
'BILL_AMT6']
df["avg_bill"] = df[bill_cols].mean(axis=1)
print(df["avg_bill"].head())  ## ye ek column banaya jo bill_amt1-6 ka avg dega in avg_bill column

pay_cols = [
'PAY_AMT1',
'PAY_AMT2',
'PAY_AMT3',
'PAY_AMT4',
'PAY_AMT5',
'PAY_AMT6']
df["avg_payment"] = df[pay_cols].mean(axis=1)

delay_cols = [
'PAY_1',
'PAY_2',
'PAY_3',
'PAY_4',
'PAY_5',
'PAY_6']
df["total_delays"] = (
    df[delay_cols] > 0
).sum(axis=1)
print(df[['PAY_1','PAY_2','total_delays']].head())

print(df[['credit_utilization','payment_ratio','avg_bill','avg_payment','total_delays']].describe())

print(
    df.groupby(
        "total_delays"
    )["default payment next month"].mean()*100)


corr = df.corr(numeric_only=True)
print(corr["default payment next month"].sort_values(ascending=False))


final_df = df[
[
"ID",
"AGE",
"LIMIT_BAL",
"PAY_1",
"total_delays",
"avg_bill",
"avg_payment",
"credit_utilization",
"default payment next month"]]
print(final_df.head())

df.to_csv('c:/code/vscode/data/credit_risk_final.csv',index=False)



