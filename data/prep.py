import pandas as pd
import glob

#Initialise aggregation lists
li_quantiles = []
li_meanIncomes = []

#Open 'continent.csv' file to add continents column
continents_csv = pd.read_csv('./continents.csv')
#Cast 'code' column to string type
continents_csv.code.astype(str)
#Drop unused columns
continents_csv = continents_csv.drop(['Three_Letter_Country_Code','Continent_Code','Country_Name','Country_Number'],axis =1)

#Open 'countries.tsv' file to add continents column
countries_tsv = pd.read_csv('./countries.tsv', sep='\t')
#Cast 'code' column to string type
countries_tsv.code.astype(str)

#Add country code to files
for fname in glob.glob('./income/*.tsv'):
    #Open '.tsv' country file
    tsv_input = pd.read_csv(fname, sep='\t')
    #Remove comment presented as a culumn
    temp = fname.find("\\")+1
    fname = fname[temp:-4]
    #Add country code as a new column
    tsv_input['code'] = fname
    #Drop unused columns
    tsv_input.drop(tsv_input.columns[6], axis=1, inplace=True) 
    #Cast 'code' to string type
    tsv_input.code.astype(str)
    #Append to the quantiles list
    li_quantiles.append(tsv_input)

#Merge each country data
frame = pd.concat(li_quantiles, axis=0, ignore_index=True)

#Add country name and country continent based on the country code column
frame = frame.merge(countries_tsv,on='code')
frame = frame.merge(continents_csv,on='code')

#Save as csv
frame.to_csv('./merged_income_quantiles.csv', index=False)

print("File 'merged_income_quantiles.csv' created succesfully !")

#Open 'income_averages.tsv' file to compute the last income average obteined
income_averages_tsv = pd.read_csv('./income_averages.tsv', sep='\t')
income_averages_tsv = income_averages_tsv.rename({'country': 'code'}, axis='columns')

#Open 'income_gini.tsv' file to compute the last GINI indicator obteined
income_gini_tsv = pd.read_csv('./income_gini.tsv', sep='\t')
income_gini_tsv = income_gini_tsv.rename({'country': 'code'}, axis='columns')

#Get last year
frame = income_averages_tsv.loc[income_averages_tsv.groupby('code')['year'].idxmax(), :]
frame_ = income_gini_tsv.loc[income_gini_tsv.groupby('code')['year'].idxmax(), :]

#Merge dataframes
frame = frame.merge(countries_tsv,on='code')
frame = frame.merge(continents_csv,on='code')
frame = frame.merge(frame_,on=['code','year'])

#Save as csv
frame.to_csv('./merged_gini_averageincome.csv', index=False)

print("File 'merged_gini_averageincome.csv' created succesfully !")
