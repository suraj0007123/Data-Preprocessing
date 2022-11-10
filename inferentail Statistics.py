import pandas as pd 
import numpy as np
import seaborn as sns
data=pd.read_excel(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\Assignment_module02 (1).xlsx")
# To know information about dataframe
data.info()

# # Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
data.Points.mean()
data.Points.median()
data.Points.mode()

# pip install numpy
from scipy import stats
stats.mode(data.Points)

# Measures of Dispersion / Second moment business decision
# Variance
data.Points.var() 

# Standard deviation
data.Points.std()

# range of column Points (Minimum range)
min(data.Points)

# range of column Points (Maximum range)
max(data.Points)


# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
data.Score.mean()
data.Score.median()
data.Score.mode()

# pip install numpy
from scipy import stats
stats.mode(data.Score)

# Measures of Dispersion / Second moment business decision
# Variance
data.Score.var()

# Standard deviation
data.Score.std()

# range of column Points (Minimum range)
min(data.Score)

# range of column Points (Maximum range)
max(data.Score)


# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
data.Weigh.mean()
data.Weigh.median()
data.Weigh.mode()

# pip install numpy
from scipy import stats
stats.mode(data.Weigh)

# Measures of Dispersion / Second moment business decision
# Variance
data.Weigh.var()

# Standard deviation
data.Weigh.std()

# range of column Points (Minimum range)
min(data.Weigh)

# range of column Points (Maximum range)
max(data.Weigh)

# lets see boxplot of each column with the help of
#######seaborn library = (Which is used Advanced data Visualization and it provides a hig-level Interface for drawing attractive and informative statistical graphical Representation ) 
sns.boxplot(data.Points)
sns.boxplot(data.Score)
sns.boxplot(data.Weigh)



import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x=pd.read_excel(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\descriptive statistics.xlsx")

# To Know the info about the dataframe 
x.info()

# Exploratory data analysis
# Measure of Central Tendency / First Moment of Business decision
# Mean (µ)
x.MeasureX.mean()

# Measures of Dispersion / Second moment business decision
# Standard Deviation (α)
x.MeasureX.std()

# Variance (α2)
x.MeasureX.var()

# Data Visualization
sns.boxplot(x.MeasureX)
plt.hist(x.MeasureX)
