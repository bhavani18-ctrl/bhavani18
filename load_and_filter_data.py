import pandas as pd
import numpy as np

df=pd.read_csv("SalesKaggle3.csv")

df_updated=df.drop(['Order','MarketingType','New_Release_Flag','SoldCount'],axis=1)

df_updated.head(1)
df_updated.to_csv('filtered_data.csv',index=False)
