################################################
#### zero variance and near zero variance ######

import pandas as pd

zdata=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\dataa-preprocessing\DataSets-Data Pre Processing\DataSets\Z_dataset.csv")

zdata.info()

zdata.shape

zdata.isna().sum()

# variance of numeric variables
zdata.var()  

zdata.Threshold=0
