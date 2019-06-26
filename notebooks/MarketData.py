#!/usr/bin/env python
# coding: utf-8

# In[4]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use("ggplot")


# In[3]:


get_ipython().system('pip install pandas-datareader')


# In[5]:


start = dt.datetime(1962, 1, 3)
end = dt.datetime(2012, 11, 9)

df = web.DataReader("^GSPC", "yahoo", start, end)
print(df.tail())


# In[6]:


pd.DataFrame(df).to_csv("^GSPC_jupyter.csv")


# In[7]:


type(df) # This was that the df is a dataframe type


# In[8]:



GSPCdf = pd.read_csv("^GSPC_jupyter.csv")
GSPCdf.head()


# In[9]:


GSPCdf = GSPCdf.assign(Returns = ((GSPCdf.Close - GSPCdf.Open) / GSPCdf.Open))
GSPCdf.head()


# In[ ]:




