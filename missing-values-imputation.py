import pandas as pd
import numpy as np
df=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\claimants.csv")

# To know the info about the dataset
df.info()

# To know the nan values each column about the dataset
df.isna().sum()

# for Mean, Meadian, Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMSEX"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMSEX"]]))
df["CLMSEX"].isna().sum()
df.isna().sum()

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMINSUR"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMINSUR"]]))
df["CLMINSUR"].isna().sum()   
df.isna().sum()

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["SEATBELT"] = pd.DataFrame(median_imputer.fit_transform(df[["SEATBELT"]]))
df["SEATBELT"].isna().sum()    
df.isna().sum()

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMAGE"]]))
df["CLMAGE"].isna().sum()  
df.isna().sum()
