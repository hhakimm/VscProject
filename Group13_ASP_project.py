import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("IMVA.xls", sheet_name="IMVA")
df1 = data[['Periods', 'Americas', 'Canada', 'USA', 'Other Markets In Americas',
             'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania',
             'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep Of)', 'Other Markets In Africa']]
newdatas = df1.replace(',', '', regex=True)
newas = newdatas.replace('na', '0', regex=True)
print(df1.columns)

print("****** First and last 3 Years Dataframe ******")
print(newas.head(3))
print(newas.tail(3))

countries = data[['Americas', 'Canada', 'USA', 'Other Markets In Americas',
             'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania',
             'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep Of)', 'Other Markets In Africa']]
print("****** Countries ******")
print(countries)

countries = countries.replace(',', '', regex=True)
countries = countries.replace('na', '0', regex=True)

# print(countries)
countries3 = countries.astype(int)
print(countries3.dtypes)
psNotSorted = countries3.sum()
print(psNotSorted)
print("****** Sorted Values ******")
psSorted = psNotSorted.sort_values(ascending=False)
print(psSorted)

newdata = df1['Periods'].str.split(' ', n=1, expand=True)
print(newdata)
df2 = data.assign(Years=newdata[1])
df2.index = df2["Years"]
graph1 = df2[(df2['Years'] >= str(1998)) & (df2['Years'] <= str(2007))]
print("****** DataFrame ******")
print(graph1)

ps = psSorted.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. Of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=5, rotation=45)
plt.title('All Other Countries from (Period:1998-2007)')
plt.bar(ps.index, ps.values/1000)
plt.savefig("All Other Countries-1998-2007.png")
plt.show()

top3 = psSorted.head(3)
print("****** Top 3 Countries ******")
print(top3)
total = top3.values.sum()
mean = round(top3.values.mean(), 2)

print("The total no. of visitors for the top 3 other country is ", total)
print('The mean values of visitor for the top 3 other country is ', mean)

ps = top3.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. Of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=5, rotation=45)
plt.title('Top 3 Others countries from (Period:1998-2007)')
plt.bar(ps.index, ps.values/1000)
plt.savefig("Top 3 Countries-1998-2007.png")
plt.show()
