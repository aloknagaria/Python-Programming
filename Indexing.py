import pandas as pd
df = pd.read_csv(r'C:\Users\Dell\Desktop\Automated File Sorter\world_population.csv', index_col="Country")
# print(df)

df.reset_index(inplace=True)
# print(df)

df.set_index('Country', inplace=True) #inplace ka use karke usko hum save kar denge df mai
# print(df)

df.reset_index(inplace=True)
# df.set_index('CCA3', inplace= True)
# print(df.loc['ASM'])

df.set_index(['Continent', 'Country'], inplace=True)
df.sort_index(inplace=True) #written this inplace to save the DataFrame df.
print(df)

# now after this sorting of the indexes the loc will search for the first column index
print(df.loc['Africa', 'Angola']) #pehle Africa ke andar ke content ko search karke dega and then the second entry provides the info of the particular index name mentioned