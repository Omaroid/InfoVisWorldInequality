import warnings
warnings.simplefilter("ignore", UserWarning)

import pandas as pd
import glob

df = pd.DataFrame(columns=["code", "year", "cumul_0_25", "cumul_25_50", "cumul_0_50", "cumul_50_75", "cumul_50_90", "cumul_75_90", "cumul_0_90", "cumul_90_95", "cumul_95_99", "cumul_99_100"])

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

    print("-----")
    print(tsv_input.code.values[0])

    for year in tsv_input.year.unique():
        
        if(tsv_input.code.values[0] == "KR" or (tsv_input.code.values[0] == "US" and year <= 1961)):
            cumul_0_90 = tsv_input[tsv_input['high'] == 0.90][tsv_input['year'] == year]['cumul'].values[0]
            cumul_90_95 = tsv_input[tsv_input['high'] == 0.95][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_90
            cumul_95_99 = tsv_input[tsv_input['high'] == 0.99][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_90-cumul_90_95
            cumul_99_100 = tsv_input[tsv_input['high'] == 1.0][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_90-cumul_90_95-cumul_95_99
            cumul_0_25 = 0
            cumul_0_50 = 0
            cumul_25_50 = 0
            cumul_50_75 = 0
            cumul_75_90 = 0
            cumul_50_90 = 0
            cumul_90_100 = 0

            df = df.append({
                "code": tsv_input.code.values[0],
                "year":  year,
                "cumul_0_25": cumul_0_25,
                "cumul_0_50": cumul_0_50,
                "cumul_25_50": cumul_25_50,
                "cumul_50_75": cumul_50_75,
                "cumul_75_90": cumul_75_90,
                "cumul_0_90": cumul_0_90,
                "cumul_90_100": cumul_90_100,
                "cumul_50_90": cumul_50_90,
                "cumul_90_95": cumul_90_95,
                "cumul_95_99": cumul_95_99,
                "cumul_99_100": cumul_99_100
                }, ignore_index=True)

        else:
            if(tsv_input.code.values[0] == "SI"):
                cumul_0_50 = tsv_input[tsv_input['high'] == 0.50][tsv_input['year'] == year]['cumul'].values[0]
                cumul_50_90 = tsv_input[tsv_input['high'] == 0.90][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_50
                cumul_90_100 = tsv_input[tsv_input['high'] == 1.0][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_50-cumul_50_90
                cumul_0_90 = 0
                cumul_90_95 = 0
                cumul_95_99 = 0
                cumul_0_25 = 0
                cumul_25_50 = 0
                cumul_50_75 = 0
                cumul_75_90 = 0
                cumul_99_100 = 0

                df = df.append({
                    "code": tsv_input.code.values[0],
                    "year":  year,
                    "cumul_0_25": cumul_0_25,
                    "cumul_0_50": cumul_0_50,
                    "cumul_25_50": cumul_25_50,
                    "cumul_50_75": cumul_50_75,
                    "cumul_75_90": cumul_75_90,
                    "cumul_0_90": cumul_0_90,
                    "cumul_90_100": cumul_90_100,
                    "cumul_50_90": cumul_50_90,
                    "cumul_90_95": cumul_90_95,
                    "cumul_95_99": cumul_95_99,
                    "cumul_99_100": cumul_99_100
                    }, ignore_index=True)

            else:
                if(tsv_input.code.values[0] == "US" and (year == 1965 or year == 1963)):
                    cumul_0_50 = tsv_input[tsv_input['high'] == 0.50][tsv_input['year'] == year]['cumul'].values[0]
                    cumul_50_90 = tsv_input[tsv_input['high'] == 0.90][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_50
                    cumul_90_95 = tsv_input[tsv_input['high'] == 0.95][tsv_input['year'] == year]['cumul'].values[0]-cumul_50_90-cumul_0_50
                    cumul_95_99 = tsv_input[tsv_input['high'] == 0.99][tsv_input['year'] == year]['cumul'].values[0]-cumul_90_95-cumul_50_90-cumul_0_50
                    cumul_99_100 = tsv_input[tsv_input['high'] == 1.0][tsv_input['year'] == year]['cumul'].values[0]-cumul_95_99-cumul_90_95-cumul_50_90-cumul_0_50
                    cumul_90_100 = 0
                    cumul_0_90 = 0
                    cumul_0_25 = 0
                    cumul_25_50 = 0
                    cumul_50_75 = 0
                    cumul_75_90 = 0

                    df = df.append({
                        "code": tsv_input.code.values[0],
                        "year":  year,
                        "cumul_0_25": cumul_0_25,
                        "cumul_0_50": cumul_0_50,
                        "cumul_25_50": cumul_25_50,
                        "cumul_50_75": cumul_50_75,
                        "cumul_75_90": cumul_75_90,
                        "cumul_0_90": cumul_0_90,
                        "cumul_90_100": cumul_90_100,
                        "cumul_50_90": cumul_50_90,
                        "cumul_90_95": cumul_90_95,
                        "cumul_95_99": cumul_95_99,
                        "cumul_99_100": cumul_99_100
                        }, ignore_index=True)
                else:
                    cumul_0_25 = tsv_input[tsv_input['high'] == 0.25][tsv_input['year'] == year]['cumul'].values[0]
                    cumul_25_50 = tsv_input[tsv_input['high'] == 0.50][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25
                    cumul_50_75 = tsv_input[tsv_input['high'] == 0.75][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25-cumul_25_50
                    cumul_75_90 = tsv_input[tsv_input['high'] == 0.90][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25-cumul_25_50-cumul_50_75
                    cumul_90_95 = tsv_input[tsv_input['high'] == 0.95][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25-cumul_25_50-cumul_50_75-cumul_75_90
                    cumul_95_99 = tsv_input[tsv_input['high'] == 0.99][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25-cumul_25_50-cumul_50_75-cumul_75_90-cumul_90_95
                    cumul_99_100 = tsv_input[tsv_input['high'] == 1.0][tsv_input['year'] == year]['cumul'].values[0]-cumul_0_25-cumul_25_50-cumul_50_75-cumul_75_90-cumul_90_95-cumul_95_99
                    cumul_0_50 = 0
                    cumul_50_90 = 0
                    cumul_90_100 = 0
                    cumul_0_90 = 0

                    df = df.append({
                        "code": tsv_input.code.values[0],
                        "year":  year,
                        "cumul_0_25": cumul_0_25,#
                        "cumul_0_50": cumul_0_50,#
                        "cumul_25_50": cumul_25_50,#
                        "cumul_50_75": cumul_50_75,
                        "cumul_75_90": cumul_75_90,
                        "cumul_0_90": cumul_0_90,
                        "cumul_90_100": cumul_90_100,
                        "cumul_50_90": cumul_50_90,
                        "cumul_90_95": cumul_90_95,
                        "cumul_95_99": cumul_95_99,
                        "cumul_99_100": cumul_99_100
                        }, ignore_index=True)

        #Verification step
        if(cumul_0_25+cumul_25_50+cumul_50_90+cumul_0_90+cumul_0_50+cumul_50_75+cumul_75_90+cumul_90_95+cumul_95_99+cumul_99_100+cumul_90_100 < 0.99 or cumul_0_25+cumul_25_50+cumul_50_90+cumul_0_90+cumul_50_75+cumul_75_90+cumul_90_95+cumul_95_99+cumul_99_100+cumul_0_50+cumul_90_100 >1.01):
            print(year)
            print(cumul_0_25+cumul_25_50+cumul_0_50+cumul_50_90+cumul_0_90+cumul_50_75+cumul_75_90+cumul_90_95+cumul_95_99+cumul_99_100+cumul_90_100)
            print("Error")

#Years problem


# #Get only last year
# idx = df.groupby(['code'])['year'].transform(max) == df['year']

# df = df[idx]
# df = df.drop("year", 1)

#To CSV
df.to_csv('./merged_quantiles.csv', index=False)

