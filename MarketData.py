#!/usr/bin/env python
# coding: utf-8

# In[69]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use("ggplot")


# In[70]:


start = dt.datetime(1962, 1, 3)
end = dt.datetime(2012, 11, 9)

df = web.DataReader("^GSPC", "yahoo", start, end)
print(df.tail())


# In[71]:


type(df) # This was that the df is a dataframe type


# In[72]:


pd.DataFrame(df).to_csv("GSPC.csv")

