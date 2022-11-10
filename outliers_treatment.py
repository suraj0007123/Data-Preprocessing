import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
Data=pd.read_csv(r"C:\Users\Sony\OneDrive\Desktop\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\boston_data.csv")
Data.info()

# Now let us check the outliers of each variables in datatset with the help boxplot 
plt.boxplot(Data.crim)
plt.boxplot(Data.zn)
plt.boxplot(Data.indus)
plt.boxplot(Data.chas)
plt.boxplot(Data.nox)
plt.boxplot(Data.rm)
plt.boxplot(Data.age)
plt.boxplot(Data.dis)
plt.boxplot(Data.rad)
plt.boxplot(Data.tax)
plt.boxplot(Data.ptratio)
plt.boxplot(Data.black)
plt.boxplot(Data.lstat)
plt.boxplot(Data.medv)



# Detection of outliers (find limits for crim based on IQR)
IQR=Data['crim'].quantile(0.75)-Data['crim'].quantile(0.25)
lower_limit=Data['crim'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['crim'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['crim'])
df_t=winsor.fit_transform(Data[['crim']])

# lets see boxplot after replacing both the values with of there outliers (Q3-Q1) with  help of Winsorization method 
sns.boxplot(df_t.crim)



# Detection of outliers (find limits for zn based on IQR)
IQR=Data['zn'].quantile(0.75)-Data['zn'].quantile(0.25)
lower_limit=Data['zn'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['zn'].quantile(0.75)+(IQR*1.5)


############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['zn'])
df_t=winsor.fit_transform(Data[['zn']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.zn)



# Detection of outliers (find limits for chas based on IQR)
IQR=Data['chas'].quantile(0.75)-Data['chas'].quantile(0.25)
lower_limit=Data['chas'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['chas'].quantile(0.75)+(IQR*1.5)


############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['chas'])
df_t=winsor.fit_transform(Data[['chas']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.chas)



# Detection of outliers (find limits for rm based on IQR)
IQR=Data['rm'].quantile(0.75)-Data['rm'].quantile(0.25)
lower_limit=Data['rm'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['rm'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['rm'])
df_t=winsor.fit_transform(Data[['rm']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.rm)



# Detection of outliers (find limits for dis based on IQR)
IQR=Data['dis'].quantile(0.75)-Data['dis'].quantile(0.25)
lower_limit=Data['dis'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['dis'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['dis'])
df_t=winsor.fit_transform(Data[['dis']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.dis)



# Detection of outliers (find limits for ptratio based on IQR)
IQR=Data['ptratio'].quantile(0.75)-Data['ptratio'].quantile(0.25)
lower_limit=Data['ptratio'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['ptratio'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['ptratio'])
df_t=winsor.fit_transform(Data[['ptratio']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.ptratio)


# Detection of outliers (find limits for black based on IQR)
IQR=Data['black'].quantile(0.75)-Data['black'].quantile(0.25)
lower_limit=Data['black'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['black'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['black'])
df_t=winsor.fit_transform(Data[['black']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.black)



# Detection of outliers (find limits for lstat based on IQR)
IQR=Data['lstat'].quantile(0.75)-Data['lstat'].quantile(0.25)
lower_limit=Data['lstat'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['lstat'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['lstat'])
df_t=winsor.fit_transform(Data[['lstat']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.lstat)



# Detection of outliers (find limits for medv based on IQR)
IQR=Data['medv'].quantile(0.75)-Data['medv'].quantile(0.25)
lower_limit=Data['medv'].quantile(0.25)-(IQR*1.5)
upper_limit=Data['medv'].quantile(0.75)+(IQR*1.5)

############### Winsorization ###############
pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',# choose  IQR rule boundaries or gaussian for mean and std
                          tail='both',# cap left, right or both tails 
                          fold=1.5,
                          variables=['medv'])
df_t=winsor.fit_transform(Data[['medv']])

# lets see boxplot after replacing the both the values with (Q3-Q1) with help of Winsorization method 
sns.boxplot(df_t.medv)

