#####################################################
######## Standardization and Normalization #########

import pandas as pd
import numpy as np

### Standardization
from sklearn.preprocessing import StandardScaler
d=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\Seeds_data.csv")
d.info()
d.head()
d.shape
d.isna().sum()
d['Type'].value_counts()
d.describe() 

# Initialise the Scaler
scaler=StandardScaler()

# To scale data
df=scaler.fit_transform(d)

# Convert the array back to a dataframe
dataset=pd.DataFrame(df)
res=dataset.describe()

### Normalization
## load data set
df1=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\Seeds_data.csv")
df1.columns

# get dummies
df1 = pd.get_dummies(df1, drop_first = True)

### Normalization function - Custom Function
# Range converts to: 0 to 1
def norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return(x)
df_norm = norm_func(df1)
b = df_norm.describe()
