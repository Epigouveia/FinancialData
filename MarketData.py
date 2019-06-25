#!/usr/bin/env python
# coding: utf-8

#### Start Header -- This is the header and contains the packages needed for this script ####

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use("ggplot")

#### End Header ####

#### Start Web Importing the financial data ####

# Here we define the date range
start = dt.datetime(1962, 1, 3)
end = dt.datetime(2012, 11, 9)

# we collect the financial date using the web.DataReader command
df = web.DataReader("^GSPC", "yahoo", start, end)
print(df.tail()) # print the last entries to see if your data is correct

# Find the type of data which was stored in df
type(df)

# save the dataframe as csv
pd.DataFrame(df).to_csv("GSPC.csv")

#### End Web Importing ####

#### Import data csv file for data process ####

^GSPC = pd.read_csv(

I am using echo to add a line at the bottom of this file
