import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\OnlineRetail.csv",encoding='unicode_escape')
df.info()
df.head()
df.describe()
df.shape
df.dtypes

# Now we convert the "float64" to "int64"
df.UnitPrice=df.UnitPrice.astype('int64')
df.dtypes

# Identifying the duplicate records from the dataset 
duplicate=df.duplicated()
duplicate
sum(duplicate)

# Removing the duplicate records from the dataset
df1=df.drop_duplicates()
print(df1.duplicated().sum())

#exploratory data analysis
# Measures of Central Tendency / First Moment of Business decision
df.Quantity.mean()
df.Quantity.median()
df.Quantity.mode()

# pip install numpy
from scipy import stats
stats.mode(df.Quantity)

# Measures of Dispersion / Second Moment of Business decision
df.Quantity.var()
df.Quantity.std()
range=max(df.Quantity)-min(df.Quantity)
range

# Third Moment of Busines decision 
df.Quantity.skew()

# Fourth Moment of Business decision
df.Quantity.kurt()

# Data Visualization (Graphical Representation)
plt.hist(df.Quantity)

plt.boxplot(df.Quantity) 

 