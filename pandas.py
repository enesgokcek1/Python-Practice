import pandas as pd
import numpy as np

#data
numbers = [20,30,40]
letters = ["a","b","c"]
scalar = 5
dict = {"a":10, "b":20, "c":30, "d":40}
random_numebers = np.random.randint(10,100,6)

pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)
pandas_series = pd.Series(scalar,[0,1,2,3])
pandas_series = pd.Series(numbers, ["a","b","c"])

result = pandas_series.dtype
result = pandas_series.shape
result = pandas_series.sum()
result = pandas_series.max()
result = pandas_series.min()
result = np.sqrt(pandas_series)
result = pandas_series =50
result = pandas_series % 2 == 0


print(pandas_series[result])
print(pandas_series)
print(result)


opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","instignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","instignia"])

total = opel2018 +opel2019
print(total)


# Pandas DataFrames

list = [["ahmet",50],["aksu",90],["ali",40],["osman",30],]
dict = {"name": ["ahmet","ali","yağmur","çınar"], "grade":[50,60,70,80]}
dict_list = [
        {"name":"ahmet","grade":50},
        {"name":"aksu","grade":90},
        {"name":"ali","grade":10},
        {"name":"osman","grade":50}
    ]
df = pd.DataFrame(list,columns =["name","grade"])
df = pd.DataFrame([1,2,3,4])
series1 = pd.Series([3,2,1,0])
series2 = pd.Series([0,3,4,1])


data = dict(apples=series1, oranges=series2)
df= pd.DataFrame(data)
print(df)
print(data)
print(dict)


#DATAFRAME

import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns =["column1", "column2", "column3"])
print(df)

dfTable = pd.DataFrame(randn(2,2), index = ["x","y"], columns = ["col1","col2"])
print(dfTable)

result = df
result = df["column1"] #tek satır seçme
result = type(df["column1"]) #tip öğrenme
result = df[["column1","column2"]]

#etiket (label) bazlı veri seçmek için kullanılır. Yani satır veya sütunları isimlerine (etiketlerine) göre seçmene olanak sağlar.
result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[:,"column1"]
result = df.loc[:,["column1","column2"]]
result = df.loc[:,:"column1"]
result = df.loc["A":,:"column2"]
result = df.loc["A","column1"]

#yeni kolon ekleme
df["column4"]= pd.Series(randn(3), ["A","B","C"])
df["column5"] = df["column2"] + df["column3"]
result = df.drop("column5", axis = 1,inplace = False)
print(result)
print(df)
#iloc indeks numarası bazlı seçim yapar
result = df.iloc[1]
print(result)



#DATAFRAME İLE FİTLRELEME

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["column1","column2","column3","column4","column5"])

result = df
result = df.columns
result = df.head()
result = df.head(10)
result = df.tail()
result = df.tail(10)
result = df["column1"].head()
result = df.column1.head()
result = df[["column1","column2"]].head()
result = df[["column1","column2"]].tail()
result = df[5:15][["column1","column2"]].head()
result = df[5:15][["column1","column2"]].tail()

result = df > 50
result = df[df > 50]
result = df[df % 2==0]
result = df[df["column1"]> 50]
result = df[(df["column1"] > 50) & (df["column2"] <= 70)] 
result = df[(df["column1"] > 50) | (df["column2"] <= 70)] 
result = df.query("column1 >= 50 & column % 2 == 0")[["column1","column2"]]
result = df.query("column1 >= 50 | column % 2 == 0")[["column1","column2"]]

print(result)








