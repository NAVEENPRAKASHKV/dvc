import pandas as pd


data={"naveen":["b tech",2013,28],
      "prakash" :["M teach",2020,25],
      "pallavi":["b tech",2013,6]
      
      }

df=pd.DataFrame(data)

df.to_csv("data/data.csv")