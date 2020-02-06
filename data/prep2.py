import pandas as pd
df1 = pd.read_csv("./income_averages.tsv", sep='\t')
df2 = pd.read_csv("./income_gini.tsv", sep='\t')

new_df = df1.merge(df2,on=['country','year'])

new_df.to_csv('./all_income_gini.csv', index=False)