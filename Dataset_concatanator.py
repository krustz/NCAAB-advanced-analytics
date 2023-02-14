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
    #finding indexes of teams
    index1 = stats_df[stats_df['Team']==row['Team_1']].index.values
    index2 = stats_df[stats_df['Team']==row['Team_2']].index.values
    #assigning the stats to the teams for the game to append them to the dataframe
    Date  = '1-31-23' #naturally this will change a lot
    Team_1 = row['Team_1']
    Team_2 = row['Team_2']
    T1AEM = stats_df.iloc[index1]['Adjusted_Efficiency_Margin'].to_string(index=False)
    T1AOE = stats_df.loc[index1]['Adjusted_Offensive_Efficency'].to_string(index=False)
    T1ADE = stats_df.loc[index1]['Adjusted_Defensive_Efficency'].to_string(index=False)
    T1AT = stats_df.loc[index1]['Adjusted_tempo'].to_string(index=False)
    T1Luck = stats_df.loc[index1]['Luck'].to_string(index=False)
    T1SOSR = stats_df.loc[index1]['Strength_of_Schedule_Rating'].to_string(index=False)
    T1AAOEOO = stats_df.loc[index1]['Adverage_Adjusted_Offensive_Efficency_of_Opponents'].to_string(index=False)
    T1AADEOO = stats_df.loc[index1]['Adverage_Adjusted_Defensive_Efficency_of_Opponents'].to_string(index=False)
    T1NCSOSR = stats_df.loc[index1]['Non_Confrence_Strength_of_Schedule_Rating'].to_string(index=False)
    T2AEM = stats_df.loc[index2]['Adjusted_Efficiency_Margin'].to_string(index=False)
    T2AOE = stats_df.loc[index2]['Adjusted_Offensive_Efficency'].to_string(index=False)
    T2ADE = stats_df.loc[index2]['Adjusted_Defensive_Efficency'].to_string(index=False)
    T2AT = stats_df.loc[index2]['Adjusted_tempo'].to_string(index=False)
    T2Luck = stats_df.loc[index2]['Luck'].to_string(index=False)
    T2SOSR = stats_df.loc[index2]['Strength_of_Schedule_Rating'].to_string(index=False)
    T2AAOEOO = stats_df.loc[index2]['Adverage_Adjusted_Offensive_Efficency_of_Opponents'].to_string(index=False)
    T2AADEOO = stats_df.loc[index2]['Adverage_Adjusted_Defensive_Efficency_of_Opponents'].to_string(index=False)
    T2NCSOSR = stats_df.loc[index2]['Non_Confrence_Strength_of_Schedule_Rating'].to_string(index=False)
    Team_1_Score = row['Team_1_Score']
    Team_2_Score = row['Team_2_Score']
    #adding game to df
    compiled_df = compiled_df.append({'Team_1':Team_1, 'Team_2':Team_2, 'T1AEM':T1AEM, 'T2AEM':T2AEM, 'Team_1_Score':Team_1_Score, 'Team_2_Score':Team_2_Score,
                                      'T1AOE':T1AOE, 'T1ADE':T1ADE, 'T1AT':T1AT, 'T1Luck':T1Luck, 'T1SOSR':T1SOSR, 'T1AAOEOO':T1AAOEOO,
                                      'T1AADEOO':T1AADEOO, 'T1NCSOSR':T1NCSOSR, 'T2AOE':T2AOE, 'T2ADE':T2ADE, 'T2AT':T2AT, 'T2Luck':T2Luck,
                                      'T2SOSR':T2SOSR, 'T2AAOEOO':T2AAOEOO, 'T2AADEOO':T2AADEOO, 'T2NCSOSR':T2NCSOSR}, ignore_index=True)
compiled_df.to_csv('compiled_stats\\cbbdata.csv', index=False)
