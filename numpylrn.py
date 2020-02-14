import numpy as np
import pandas as pd


x=pd.read_csv("D:\email\CSV\combined_csv.csv")
print(x.describe())
# s=pd.Series({1, 2, 3})
# print(s)
print(x.iloc[:3,:4])
print(x.loc[:"1",:"Ms Id"])
# print(x)
# print(x.sum(axis=0))
# print(x.index)
# print(x.columns)
# print(x['a'])
# pp=pd.Series(np.linspace(1,10,3))
# print(pp)

# y=pd.DataFrame({'one':pd.Series(range(5)),
#                  'two':pd.Series(range(5,10)),
#                  'three':pd.Series(list('abcde'))
#                   
#                  })
# print(y)
# print(y)
# y['Four']={"s","g","df","m","p"}
# print(y)
# print(y.iloc[1:3,2:4])
# print(np.cumsum(y.iloc[1:3,2:4], axis=1))

# aa=pd.DataFrame({'one':pd.Series(range(5)),
#                  'two':pd.Series(range(5)),
#                  'three':pd.Series(range(5))
#                  
#                  })
# print(aa)