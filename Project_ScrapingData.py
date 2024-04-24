from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')
# print(soup)
table = soup.find_all('table', class_ = "wikitable sortable")[0]
# print(table)

# world_titles = soup.find_all('th')
world_titles = table.find_all('th')
# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)

import pandas as pd
df = pd.DataFrame(columns = world_table_titles)
# print(df)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
print(df)

df.to_csv(r'C:\Users\Dell\Desktop\Automated File Sorter\csv files\ShortTermTrades.csv', index = False)