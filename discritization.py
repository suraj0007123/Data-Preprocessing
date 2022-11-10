import pandas as pd
import numpy as np
data=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\iris.csv")
data.head()
# To know the Information of iris.dataset 
data.info()
# To Know the stats about iris dataset
data.describe()
# To know the shape of iris dataset
data.shape

# To display no.of sample of each class
data['Species'].value_counts()

# To Check for null values
data.isnull().sum()

# Discritization of each variable with labels (Low , High)
data['Sepal.Length_new'] = pd.cut(data['Sepal.Length'], bins=[min(data['Sepal.Length']) - 1,data['Sepal.Length'].mean(), max(data['Sepal.Length'])], labels=["Low","High"])

data['Sepal.Width_new'] = pd.cut(data['Sepal.Width'], bins=[min(data['Sepal.Width']) - 1,data['Sepal.Width'].mean(), max(data['Sepal.Width'])], labels=["Low","High"])

data['Petal.Length_new'] = pd.cut(data['Petal.Length'], bins=[min(data['Petal.Length']) - 1,data['Petal.Length'].mean(), max(data['Petal.Length'])], labels=["Low","High"])

data['Petal.Width_new'] = pd.cut(data['Petal.Width'], bins=[min(data['Petal.Width']) - 1,data['Petal.Width'].mean(), max(data['Petal.Width'])], labels=["Low","High"])

# After  Discritization of each variable with labels (Low , High)
# Let us count the unique values in a single column of each variable in the dataset  
data['Sepal.Length_new'].value_counts()                                                          

data['Sepal.Width_new'].value_counts()

data['Petal.Length_new'].value_counts()

data['Petal.Width_new'].value_counts()

#Let’s create a new column called ‘SepalLength_Size’ which contains “High” if Sepal Length ≥ 5 or “Low” if Sepal Length < 5.
# Create column based on conditions
data['Sepal.Length_Size'] = np.where(data['Sepal.Length']>=5,'High','Low')


data['Sepal.Length_Size'] = ['High' if x >= 5 else 'Low' for x in data['Sepal.Length'] ]

#Now, let’s create the column using the ‘assign’ function in pandas dataframe
def size(row_number):
    if row_number["Sepal.Length"] >=5:
        return 'High'
    else:
        return 'Low'

# Unique values of column
data['Species'].unique()

# With the help of CrossTabulation function 
#Let’s use the columns ‘Name’ and ‘SepalLength_Size’ 
pd.crosstab(data['Species'],data['Sepal.Length_Size'])

# Sorting values
# Let’s sort the data by ‘Sepal Length’.
data.sort_values('Sepal.Length')

#Binning numerical columns
#Create a new column in the iris dataset
bins = [0, 1, 2, 3, 4, 5,6,7]
data['bins'] = pd.cut(data['Sepal.Length'], bins)
data.dtypes
