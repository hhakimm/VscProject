import pandas as pd  # Import Library
import matplotlib.pyplot as plt  # Import Library
import numpy as np  # Import Library

# Q1
excel = pd.read_excel("IMVA.xls", sheet_name="IMVA")  # Read Excel file and from sheet IMVA
dataframe1 = excel[['Periods', 'Americas', 'Canada', 'USA', 'Other Markets In Americas',
             'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania',
             'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep Of)', 'Other Markets In Africa']]  # Make new dataframe
newData = dataframe1.replace(',', '', regex=True)  # Replacing integer
repData = newData.replace('na', '0', regex=True)  # Replacing integer
print(dataframe1.columns)  # Printing of column

# Q2
print("*****First and last 3 years dataframe*****")
print(repData.head(3))  # Print first Top 3 years
print(repData.tail(3))  # Print last bottom 3 years

# Q3
print("*****sorted values*****")  # Print string
countries = excel[['Americas', 'Canada', 'USA', 'Other Markets In Americas',
             'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania',
             'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep Of)', 'Other Markets In Africa']]  # Make new dataframe
countries = countries.replace(',', '', regex=True)  # Replacing integer
countries = countries.replace('na', '0', regex=True)  # Replacing integer
countries3 = countries.astype(int)  # Set the type as integer
psNotSorted = countries3.sum()
psSorted = psNotSorted.sort_values(ascending=False)
print(psSorted)

# Q4
print("*****Top 3 countries*****")
top3 = psSorted.head(3)
print(top3)
total = top3.values.sum()
mean = round(top3.values.mean(), 2)
print("*****Total and mean value of the top 3 countries*****")
print("The total no. of visitors for the top 3 other country is ", total)
print("The mean values for the top 3 other country is ", mean)

# Q5
newData = dataframe1['Periods'].str.split(' ', n=1, expand=True)
# print(newData)
dataframe2 = excel.assign(Years=newData[1])
dataframe2.index = dataframe2["Years"]
chart1 = dataframe2[(dataframe2['Years'] >= str(1998)) & (dataframe2['Years'] <= str(2007))]

ps = psSorted.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. Of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=8, rotation=80)
plt.title('All Other Countries from (Period:1998-2007)')
plt.bar(ps.index, ps.values/1000)
plt.savefig("All Other Countries-1998-2007.png")
plt.show()

# Q6
ps = top3.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. Of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=8, rotation=80)
plt.title('Top 3 other countries from (Period:1998-2007)')
plt.bar(ps.index, ps.values/1000)
plt.savefig("Top 3 Countries-1998-2007.png")
plt.show()
