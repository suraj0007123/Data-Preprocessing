import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_1 = pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\animal_category.csv")

# column names
df_1.columns

# will give u shape of the dataframe
df_1.shape 

# To know the info about the dataset 
df_1.info()

# To know the data of each variable in the dataset 
df_1.dtypes

# drop emp_name column
df_1.drop(['Index','Animals'], axis=1,inplace=True)
df_1.dtypes

# Now Creating the Dummy Variables 
df_new = pd.get_dummies(df_1)
df_new_1 = pd.get_dummies(df_1, drop_first=True)
# We have created dummies for all the categorical columns 


######## One Hot Encoding Works #########
df_1.columns
df = df_1[['Homly', 'Types']]

# Import library called One OneHotEncoder from sklearn.preprocessing 
from sklearn.preprocessing import OneHotEncoder
# Creating the Instance of OneHotEncoder
enc = OneHotEncoder() # Initializing method

enc_df = pd.DataFrame(enc.fit_transform(df.iloc[:, 2:]).toarray())
