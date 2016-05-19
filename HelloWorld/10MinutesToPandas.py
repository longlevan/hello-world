__author__ = 'Louis Le'
# This is a short introduction to pandas, geared mainly for new users. You can see more complex recipes in the Cookbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# Object creation
# See the Data Structure Intro section
"Creating a Series by passing a list of values, letting pandas create a default integer index"
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
"Creating a dataframe by passing a numpy array, with a datetime index and labeled columns"
dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['value 1','value 2','value 3','value 4'])
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D': np.array([3]*4,dtype='int32'),
                    'E': pd.Categorical(["text","train","test","train"]),
                    'F' : 'foo'})
print(df2)

plt.plot(range(100))

print(df)


help(pd.DataFrame.drop)

df = df[df.xs('value 1',axis=1) <0]
print(df)