import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("IMVA.xls", sheet_name="IMVA")
newdata=data[['Periods','Americas', 'Canada', 'USA', 'Other Markets In Americas',
             'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania',
             'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep Of)','Other Markets In Africa']]
newdatas=newdata.replace(',','', regex=True)
newas=newdatas.replace('na','0',regex=True)
print(newdata.index)
print(newdata.columns)
print(newas.head(3))
print(newas.tail(3))
datas = newdata['Periods'].str.split(' ', n=1, expand=True)
print(datas)






