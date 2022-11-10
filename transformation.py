######## Transformation ########
import pandas as pd
df=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\calories_consumed.csv")
df.head()
df.columns

# Rename the columns 
df.rename(columns={'Weight gained (grams)':'Weightgained_grams','Calories Consumed':"Calories_consumed"}, inplace=True)
df.columns

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# boxplot
sns.boxplot(df.Weightgained_grams)

# Histogram
plt.hist(df.Weightgained_grams,color='red')

# Transformation to make workex variable normal
plt.hist(np.log(df.Weightgained_grams))

# boxplot
sns.boxplot(df.Calories_consumed)

# Histogram
plt.hist(df.Calories_consumed,color='orange')

# Transformation to make workex variable normal
plt.hist(np.log(df.Calories_consumed))
