import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')

table = soup.find_all('table', class_='dataTable')[0]
# print(table)

country_titles = []
for th in table.find_all('th'):
    first_text = th.find('span').text
    country_titles.append(first_text)
# print(country_titles)

df = pd.DataFrame(columns = country_titles)
column_data = table.find_all('tr')
# print(column_data)
# print(country_table_titles)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = []
    for irdata in row_data:
        individual_row_data.append(irdata.text.strip())
    length = len(df)
    df.loc[length] = individual_row_data
print(df)

df.to_csv(r'C:\Users\Dell\Desktop\Automated File Sorter\csv files\FailedBanks.csv', index=False)

df1 = pd.read_csv('C:/Users/Dell/Desktop/Automated File Sorter/csv files/FailedBanks.csv')
# print(df1.head())
# print(df1.columns)
df1 = df1.drop(['Cert', 'Fund'], axis=1)
# print(df1.head())

print(df1['City'].value_counts()) #iska mtlb value ke kitne counts hain
# print(df1.dtypes)

df1['Closing Date']= pd.to_datetime(df1['Closing Date'])
print(df1.head())

ycounts = df1.groupby(df1['Closing Date'].dt.year).size()

ycounts.plot(kind='line', color='green')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Bank Failed per year')
plt.show()