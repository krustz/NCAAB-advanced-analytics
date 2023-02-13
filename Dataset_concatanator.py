#Dataset_concatanator.py
#Cullen Wise
#created 2-13-23
#this program concatnates scores and stats into a nice format for our machince learning applications
#PLEASE NOTE this will have filepaths in the code being altered frequently to add more or different data

import pandas as pd
import warnings

warnings.filterwarnings("ignore")
#ignoring warnings

compiled_df = pd.read_csv('compiled_stats\\cbbdata.csv')
#headers in compiled Date,Team_1,Team_2,T1AEM,T1AOE,T1ADE,T1AT,T1Luck,T1SOSR,T1AAOEOO,T1AADEOO,T1NCSOSR,
#T2AEM,T2AOE,T2ADE,T2AT,T2Luck,T2SOSR,T2AAOEOO,T2AADEOO,T2NCSOSR,Team_1_Score,Team_2_Score


#these are the files made by the two web scrapers in this project and the names of files are sujbest to change
games_df = pd.read_csv('games\\scores1-31-23.csv')
stats_df = pd.read_csv('stats\\stats1-31-23.csv')

for index, row in games_df.iterrows():
    print(row['Team_1'],row['Team_2'], '\n', row['Team_1_Score'],row['Team_2_Score'])
    index1 = stats_df[stats_df['Team']==row['Team_1']].index.values
    index2 = stats_df[stats_df['Team']==row['Team_2']].index.values
    #print(stats_df.loc[index1])
    #print(stats_df.loc[index2])
    Date  = '1-31-23' #naturally this will change a lot
    Team_1 = row['Team_1']
    Team_2 = row['Team_2']
    T1AEM = stats_df.loc[index1,4]
    T1AOE = stats_df.loc[index1,5]
    T1ADE = stats_df.loc[index1,6]
    T1AT = stats_df.loc[index1,7]
    T1Luck = stats_df.loc[index1,8]
    T1SOSR = stats_df.loc[index1,9]
    T1AAOEOO = stats_df.loc[index1,10]
    T1AADEOO = stats_df.loc[index1,11]
    T1NCSOSR = stats_df.loc[index1,12]
    T2AEM = stats_df.loc[index2,4]
    T2AOE = stats_df.loc[index2,5]
    T2ADE = stats_df.loc[index2,6]
    T2AT = stats_df.loc[index2,7]
    T2Luck = stats_df.loc[index2,8]
    T2SOSR = stats_df.loc[index2,9]
    T2AAOEOO = stats_df.loc[index2,10]
    T2AADEOO = stats_df.loc[index2,11]
    T2NCSOSR = stats_df.loc[index2,12]
    Team_1_Score = row['Team_1_Score']
    Team_2_Score = row['Team_2_Score']
    
    compiled_df = compiled_df.append({'Team_1':Team_1, 'Team_2':Team_2, 'T1AEM':T1AEM, 'T2AEM':T2AEM, 'Team_1_Score':Team_1_Score, 'Team_2_Score':Team_2_Score}, ignore_index=True)
