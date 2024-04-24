import pandas as pd
import openpyxl
df = pd.read_csv(r"C:\Users\Dell\Desktop\Automated File Sorter\world_population.csv")
# pd.set_option('display.max.rows', None)
# df = df.iloc[0:, 0:5]
# print(df)

filter_modification = df['Rank']<10 #yaha pe ye boolean values return karega kyonki pandas mai esa hi hota hai and jab true values ayegi to df mai dal ke print ho jayegi
print(df[filter_modification])

specific_countries = ['Bangladesh', 'Brazil']
check_countries = df['Country'].isin(specific_countries) #this returns the true values present in the df and then applying in the df can give the true value output.
print(df[check_countries])

print(df[df['Country'].str.contains('United')]) #for searching with the word containing in the column Country

df2 = df.set_index('Country')
print(df2.filter(items = ['Country', 'CCA3', 'Rank'], axis=1))
print(df2.filter(items = ['Zimbabwe'], axis=0))
print(df2.filter(like = 'United', axis = 0))
print(df2.loc['United States'])
print(df2.iloc[3])

print(df[df['Rank']<10].sort_values(by = 'Rank', ascending=True))
print(df[df['Rank']<10].sort_values(by = ['Continent', 'Country'], ascending=[False, True])) #ye isiliye ki define karna hai ki kis column ke according sort karna hai.