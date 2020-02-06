import pandas as pd
df1 = pd.read_csv("./gdp_growth.tsv", sep='\t')
df2 = pd.read_csv("./gini.tsv", sep='\t')

new_df = df1.merge(df2,on=['country','year'])
print(new_df.country.nunique())

new_df.to_csv('./BRICS_growth_gini.csv', index=False)