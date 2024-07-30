import pandas as pd 
import numpy as np

# ************************************Series in Pandas *********************************************

series_1 = pd.Series(data=["Ali", "Hareem", "Zainab","Fatima"])
print(series_1)

series_2 = pd.Series(data=["Ali", "Hareem", "Zainab","Fatima"],index =[44,55,66,77])
print(series_2)
series_3 = pd.Series(np.arange(1,10))
print(series_3)

series_4 = pd.Series({"name":"ali","gender":"Male","registration no ": "789875"})
print(series_4)

series_5 = pd.Series(5)
print(series_5)

series_6 = pd.Series(dtype= "float64")
print(series_6)
# ************************************Attributes in Pandas Series*********************************************
print(series_1)
print(series_1.name)
print(series_1.dtype)
print(series_1.ndim)
print(series_1.size)
print(series_1.shape)
print(series_1.index)
print(series_1.values)
print(series_1.value_counts)

# ************************************Understanding Index in Series*********************************************

indexes = np.arange(4)
series_1.index = indexes
print(series_1)
#                                              Use of Indexes
print("Value of second index ",series_1[2])
print(series_1.loc[2])
print(series_1.iloc[2])

#                                              Access Multiple values by using  Indexes
print(series_1[[1,3]])
print(series_1.loc[[0,2]])
print(series_1.iloc[[1,3]])

#                                              Use of index in Slicing
print(series_1[1:3])
print(series_1.loc[0:2])
print(series_1.iloc[1:3])


#                                              Addition of two series
serie_1 = pd.Series(np.random.randint(1,10,5))
serie_2 = pd.Series(np.random.randint(1,10,5))
serie_NO_3 = serie_1+serie_2
print("Addition of two series : \n",serie_NO_3)
