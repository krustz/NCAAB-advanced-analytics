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
games_df = pd.read_csv('games\\scores2-2-23.csv')
stats_df = pd.read_csv('stats\\stats1-31-23.csv')

for index, row in games_df.iterrows():
    #finding indexes of teams
    index1 = stats_df[stats_df['Team']==row['Team_1']].index.values
    index2 = stats_df[stats_df['Team']==row['Team_2']].index.values

    #if a team doesnt have a name that matches up this should fix it
    if(not index1.any()):
        
        
        if(row['Team_1']=='Miami (FL)'):
            index1 = stats_df[stats_df['Team']=='Miami FL'].index.values
        if(row['Team_1']=='Miami (OH)'):
            index1 = stats_df[stats_df['Team']=='Miami OH'].index.values
        if(row['Team_1']=='Central Mich.'):
            index1 = stats_df[stats_df['Team']=='Central Michigan'].index.values
        if(row['Team_1']=='NIU'):
            index1 = stats_df[stats_df['Team']=='Northern Illinois'].index.values
        if(row['Team_1']=='Western Mich.'):
            index1 = stats_df[stats_df['Team']=='Western Michigan'].index.values
        if(row['Team_1']=='Eastern Mich.'):
            index1 = stats_df[stats_df['Team']=='Eastern Michigan'].index.values
        if(row['Team_1']=='UConn'):
            index1 = stats_df[stats_df['Team']=='Connecticut'].index.values
        if(row['Team_1']=='Ole Miss'):
            index1 = stats_df[stats_df['Team']=='Mississippi'].index.values

        if(row['Team_1']=='UAlbany'):
            index1 = stats_df[stats_df['Team']=='Albany'].index.values
        if(row['Team_1']=='South Fla.'):
            index1 = stats_df[stats_df['Team']=='South Florida'].index.values
        if(row['Team_1']=='ETSU'):
            index1 = stats_df[stats_df['Team']=='East Tennessee St.'].index.values
        if(row['Team_1']=='Boston U.'):
            index1 = stats_df[stats_df['Team']=='Boston University'].index.values
        if(row['Team_1']=='Army West Point'):
            index1 = stats_df[stats_df['Team']=='Army'].index.values
        if(row['Team_1']=='Western Caro.'):
            index1 = stats_df[stats_df['Team']=='Western Carolina'].index.values
        if(row['Team_1']=='Gardner-Webb'):
            index1 = stats_df[stats_df['Team']=='Gardner Webb'].index.values
        if(row['Team_1']=='Charleston So.'):
            index1 = stats_df[stats_df['Team']=='Charleston Southern'].index.values
        if(row['Team_1']=='Sam Houston'):
            index1 = stats_df[stats_df['Team']=='Sam Houston St.'].index.values
        if(row['Team_1']=='UTRGV'):
            index1 = stats_df[stats_df['Team']=='UT Rio Grande Valley'].index.values
        if(row['Team_1']=='Southern Ill.'):
            index1 = stats_df[stats_df['Team']=='Southern Illinois'].index.values
        if(row['Team_1']=='UIC'):
            index1 = stats_df[stats_df['Team']=='Illinois Chicago'].index.values
        if(row['Team_1']=="St. John's (NY)"):
            index1 = stats_df[stats_df['Team']=="St. John's"].index.values
        if(row['Team_1']=='NC State'):
            index1 = stats_df[stats_df['Team']=="N.C. State"].index.values
        if(row['Team_1']=='UNI'):
            index1 = stats_df[stats_df['Team']=='Northern Iowa'].index.values
        if(row['Team_1']=='SFA'):
            index1 = stats_df[stats_df['Team']=='Stephen F. Austin'].index.values
        if(row['Team_1']=='California Baptist'):
            index1 = stats_df[stats_df['Team']=='Cal Baptist'].index.values
        if(row['Team_1']=='Seattle U'):
            index1 = stats_df[stats_df['Team']=='Seattle'].index.values


#seperation comment 
        if(row['Team_1']=='Central Conn. St.'):
            index1 = stats_df[stats_df['Team']=='Central Connectitcut'].index.values
        if(row['Team_1']=='St. Francis Brooklyn'):
            index1 = stats_df[stats_df['Team']=='St. Francis NY'].index.values
        if(row['Team_1']=='App State'):
            index1 = stats_df[stats_df['Team']=='Appalachian St.'].index.values
        if(row['Team_1']=='N.C. A&T'):
            index1 = stats_df[stats_df['Team']=='North Carolina A&T'].index.values
        if(row['Team_1']=='UNCW'):
            index1 = stats_df[stats_df['Team']=='UNC Wilmington'].index.values
        if(row['Team_1']=='UT Martin'):
            index1 = stats_df[stats_df['Team']=='Tennessee Martin'].index.values
        if(row['Team_1']=='SIUE'):
            index1 = stats_df[stats_df['Team']=='Southern Illinois'].index.values
        if(row['Team_1']=='Central Ark.'):
            index1 = stats_df[stats_df['Team']=='Central Arkansas'].index.values
        if(row['Team_1']=='FGCU'):
            index1 = stats_df[stats_df['Team']=='Florida Gulf Coast'].index.values
        if(row['Team_1']=='Col. of Charleston'):
            index1 = stats_df[stats_df['Team']=='Charleston'].index.values
        if(row['Team_1']=='Fla. Atlantic'):
            index1 = stats_df[stats_df['Team']=='Florida Atlantic'].index.values
        if(row['Team_1']=='Saint Francis (PA)'):
            index1 = stats_df[stats_df['Team']=='St. Francis PA'].index.values
        if(row['Team_1']=='North Ala.'):
            index1 = stats_df[stats_df['Team']=='North Alabama'].index.values
        #not sure what to do is stats dont exist giving worst stats to this team
        #if(row['Team_1']=='Regent'):
            

        if(row['Team_1']=='UMES'):
            index1 = stats_df[stats_df['Team']=='Maryland Eastern Shore'].index.values
        if(row['Team_1']=='Southern Miss.'):
            index1 = stats_df[stats_df['Team']=='Southern Miss'].index.values
        if(row['Team_1']=='Northern Ky.'):
            index1 = stats_df[stats_df['Team']=='Northern Kentucky'].index.values
        if(row['Team_1']=='Ga. Southern'):
            index1 = stats_df[stats_df['Team']=='Georgia Southern'].index.values
        if(row['Team_1']=='Eastern Ky.'):
            index1 = stats_df[stats_df['Team']=='Eastern Kentucky'].index.values
        if(row['Team_1']=='ULM'):
            index1 = stats_df[stats_df['Team']=='Louisiana Monroe'].index.values
        if(row['Team_1']=='St. Thomas (MN)'):
            index1 = stats_df[stats_df['Team']=='St. Thomas'].index.values
        if(row['Team_1']=='Omaha'):
            index1 = stats_df[stats_df['Team']=='Nebraska Omaha'].index.values
        if(row['Team_1']=='Eastern Ill.'):
            index1 = stats_df[stats_df['Team']=='Eastern Illinois'].index.values
        if(row['Team_1']=='Queens (NC)'):
            index1 = stats_df[stats_df['Team']=='Queens'].index.values
        if(row['Team_1']=='Western Ky.'):
            index1 = stats_df[stats_df['Team']=='Western Kentucky'].index.values
        if(row['Team_1']=='Southeast Mo. St.'):
            index1 = stats_df[stats_df['Team']=='Southeast Missouri St.'].index.values
        if(row['Team_1']=='A&M-Corpus Christi'):
            index1 = stats_df[stats_df['Team']=='Texas A&M Corpus Chris'].index.values
        if(row['Team_1']=='Southern Ind.'):
            index1 = stats_df[stats_df['Team']=='Southern Indiana'].index.values
        if(row['Team_1']=='UIW'):
            index1 = stats_df[stats_df['Team']=='Incarnate Word'].index.values
        if(row['Team_1']=='Southeastern La.'):
            index1 = stats_df[stats_df['Team']=='Southeastern Louisiana'].index.values
        if(row['Team_1']=='Lamar University'):
            index1 = stats_df[stats_df['Team']=='Lamar'].index.values
        if(row['Team_1']=='McNeese'):
            index1 = stats_df[stats_df['Team']=='McNeese St.'].index.values
        if(row['Team_1']=='LMU (CA)'):
            index1 = stats_df[stats_df['Team']=='Loyola Marymount'].index.values
        if(row['Team_1']=='Middle Tenn.'):
            index1 = stats_df[stats_df['Team']=='Middle Tennessee'].index.values
        if(row['Team_1']=='Western Ill.'):
            index1 = stats_df[stats_df['Team']=='Western Illinois'].index.values
        if(row['Team_1']=='Northern Colo.'):
            index1 = stats_df[stats_df['Team']=='Northern Colorado'].index.values
        if(row['Team_1']=='Northern Ariz.'):
            index1 = stats_df[stats_df['Team']=='Northern Arizona'].index.values
        if(row['Team_1']=='Eastern Wash.'):
            index1 = stats_df[stats_df['Team']=='Eastern Washington'].index.values
        if(row['Team_1']=='CSU Bakersfield'):
            index1 = stats_df[stats_df['Team']=='Cal St. Bakersfield'].index.values
        if(row['Team_1']=='Southern California'):
            index1 = stats_df[stats_df['Team']=='USC'].index.values
        if(row['Team_1']=="Saint Mary's (CA)"):
            index1 = stats_df[stats_df['Team']=="Saint Mary's"].index.values
        if(row['Team_1']=="Central Conn. St."):
            index1 = stats_df[stats_df['Team']=="Central Connecticut"].index.values
     
        
    if(not index2.any()):
 
        if(row['Team_2']=='Miami (FL)'): 
            index2 = stats_df[stats_df['Team']=='Miami FL'].index.values
        if(row['Team_2']=='Miami (OH)'):
            index2 = stats_df[stats_df['Team']=='Miami OH'].index.values
        if(row['Team_2']=='Central Mich.'):
            index2 = stats_df[stats_df['Team']=='Central Michigan'].index.values
        if(row['Team_2']=='NIU'):
            index2 = stats_df[stats_df['Team']=='Northern Illinois'].index.values
        if(row['Team_2']=='Western Mich.'):
            index2 = stats_df[stats_df['Team']=='Western Michigan'].index.values
        if(row['Team_2']=='Eastern Mich.'):
            index2 = stats_df[stats_df['Team']=='Eastern Michigan'].index.values
        if(row['Team_2']=='UConn'):
            index2 = stats_df[stats_df['Team']=='Connecticut'].index.values
        if(row['Team_2']=='Ole Miss'):
            index2 = stats_df[stats_df['Team']=='Mississippi'].index.values

        if(row['Team_2']=='UAlbany'):
            index2 = stats_df[stats_df['Team']=='Albany'].index.values
        if(row['Team_2']=='South Fla.'):
            index2 = stats_df[stats_df['Team']=='South Florida'].index.values
        if(row['Team_2']=='ETSU'):
            index2 = stats_df[stats_df['Team']=='East Tennessee St.'].index.values
        if(row['Team_2']=='Boston U.'):
            index2 = stats_df[stats_df['Team']=='Boston University'].index.values
        if(row['Team_2']=='Army West Point'):
            index2 = stats_df[stats_df['Team']=='Army'].index.values
        if(row['Team_2']=='Western Caro.'):
            index2 = stats_df[stats_df['Team']=='Western Carolina'].index.values
        if(row['Team_2']=='Gardner-Webb'):
            index2 = stats_df[stats_df['Team']=='Gardner Webb'].index.values
        if(row['Team_2']=='Charleston So.'):
            index2 = stats_df[stats_df['Team']=='Charleston Southern'].index.values
        if(row['Team_2']=='Sam Houston'):
            index2 = stats_df[stats_df['Team']=='Sam Houston St.'].index.values
        if(row['Team_2']=='UTRGV'):
            index2 = stats_df[stats_df['Team']=='UT Rio Grande Valley'].index.values
        if(row['Team_2']=='Southern Ill.'):
            index2 = stats_df[stats_df['Team']=='Southern Illinois'].index.values
        if(row['Team_2']=='UIC'):
            index2 = stats_df[stats_df['Team']=='Illinois Chicago'].index.values
        if(row['Team_2']=="St. John's (NY)"):
            index2 = stats_df[stats_df['Team']=="St. John's"].index.values
        if(row['Team_2']=='NC State'):
            index2 = stats_df[stats_df['Team']=="N.C. State"].index.values
        if(row['Team_2']=='UNI'):
            index2 = stats_df[stats_df['Team']=='Northern Iowa'].index.values
        if(row['Team_2']=='SFA'):
            index2 = stats_df[stats_df['Team']=='Stephen F. Austin'].index.values
        if(row['Team_2']=='California Baptist'):
            index2 = stats_df[stats_df['Team']=='Cal Baptist'].index.values
        if(row['Team_2']=='Seattle U'):
            index2 = stats_df[stats_df['Team']=='Seattle'].index.values
            #seperation comment
        if(row['Team_2']=='Central Conn. St.'):
            index2 = stats_df[stats_df['Team']=='Central Connectitcut'].index.values
        if(row['Team_2']=='St. Francis Brooklyn'):
            index2 = stats_df[stats_df['Team']=='St. Francis NY'].index.values
        if(row['Team_2']=='App State'):
            index2 = stats_df[stats_df['Team']=='Appalachian St.'].index.values
        if(row['Team_2']=='N.C. A&T'):
            index2 = stats_df[stats_df['Team']=='North Carolina A&T'].index.values
        if(row['Team_2']=='UNCW'):
            index2 = stats_df[stats_df['Team']=='UNC Wilmington'].index.values
        if(row['Team_2']=='UT Martin'):
            index2 = stats_df[stats_df['Team']=='Tennessee Martin'].index.values
        if(row['Team_2']=='SIUE'):
            index2 = stats_df[stats_df['Team']=='Southern Illinois'].index.values
        if(row['Team_2']=='Central Ark.'):
            index2 = stats_df[stats_df['Team']=='Central Arkansas'].index.values
        if(row['Team_2']=='FGCU'):
            index2 = stats_df[stats_df['Team']=='Florida Gulf Coast'].index.values
        if(row['Team_2']=='Col. of Charleston'):
            index2 = stats_df[stats_df['Team']=='Charleston'].index.values
        if(row['Team_2']=='Fla. Atlantic'):
            index2 = stats_df[stats_df['Team']=='Florida Atlantic'].index.values
        if(row['Team_2']=='Saint Francis (PA)'):
            index2 = stats_df[stats_df['Team']=='St. Francis PA'].index.values
        if(row['Team_2']=='North Ala.'):
            index2 = stats_df[stats_df['Team']=='North Alabama'].index.values
        #not sure what to do is stats dont exist giving worst stats to this team
        #if(row['Team_2']=='Regent'):
            

        if(row['Team_2']=='UMES'):
            index2 = stats_df[stats_df['Team']=='Maryland Eastern Shore'].index.values
        if(row['Team_2']=='Southern Miss.'):
            index2 = stats_df[stats_df['Team']=='Southern Miss'].index.values
        if(row['Team_2']=='Northern Ky.'):
            index2 = stats_df[stats_df['Team']=='Northern Kentucky'].index.values
        if(row['Team_2']=='Ga. Southern'):
            index2 = stats_df[stats_df['Team']=='Georgia Southern'].index.values
        if(row['Team_2']=='Eastern Ky.'):
            index2 = stats_df[stats_df['Team']=='Eastern Kentucky'].index.values
        if(row['Team_2']=='ULM'):
            index2 = stats_df[stats_df['Team']=='Louisiana Monroe'].index.values
        if(row['Team_2']=='St. Thomas (MN)'):
            index2 = stats_df[stats_df['Team']=='St. Thomas'].index.values
        if(row['Team_2']=='Omaha'):
            index2 = stats_df[stats_df['Team']=='Nebraska Omaha'].index.values
        if(row['Team_2']=='Eastern Ill.'):
            index2 = stats_df[stats_df['Team']=='Eastern Illinois'].index.values
        if(row['Team_2']=='Queens (NC)'):
            index2 = stats_df[stats_df['Team']=='Queens'].index.values
        if(row['Team_2']=='Western Ky.'):
            index2 = stats_df[stats_df['Team']=='Western Kentucky'].index.values
        if(row['Team_2']=='Southeast Mo. St.'):
            index2 = stats_df[stats_df['Team']=='Southeast Missouri St.'].index.values
        if(row['Team_2']=='A&M-Corpus Christi'):
            index2 = stats_df[stats_df['Team']=='Texas A&M Corpus Chris'].index.values
        if(row['Team_2']=='Southern Ind.'):
            index2 = stats_df[stats_df['Team']=='Southern Indiana'].index.values
        if(row['Team_2']=='UIW'):
            index2 = stats_df[stats_df['Team']=='Incarnate Word'].index.values
        if(row['Team_2']=='Southeastern La.'):
            index2 = stats_df[stats_df['Team']=='Southeastern Louisiana'].index.values
        if(row['Team_2']=='Lamar University'):
            index2 = stats_df[stats_df['Team']=='Lamar'].index.values
        if(row['Team_2']=='McNeese'):
            index2 = stats_df[stats_df['Team']=='McNeese St.'].index.values
        if(row['Team_2']=='LMU (CA)'):
            index2 = stats_df[stats_df['Team']=='Loyola Marymount'].index.values
        if(row['Team_2']=='Middle Tenn.'):
            index2 = stats_df[stats_df['Team']=='Middle Tennessee'].index.values
        if(row['Team_2']=='Western Ill.'):
            index2 = stats_df[stats_df['Team']=='Western Illinois'].index.values
        if(row['Team_2']=='Northern Colo.'):
            index2 = stats_df[stats_df['Team']=='Northern Colorado'].index.values
        if(row['Team_2']=='Northern Ariz.'):
            index2 = stats_df[stats_df['Team']=='Northern Arizona'].index.values
        if(row['Team_2']=='Eastern Wash.'):
            index2 = stats_df[stats_df['Team']=='Eastern Washington'].index.values
        if(row['Team_2']=='CSU Bakersfield'):
            index2 = stats_df[stats_df['Team']=='Cal St. Bakersfield'].index.values
        if(row['Team_2']=='Southern California'):
            index2 = stats_df[stats_df['Team']=='USC'].index.values
        if(row['Team_2']=="Saint Mary's (CA)"):
            index2 = stats_df[stats_df['Team']=="Saint Mary's"].index.values
        if(row['Team_2']=="Central Conn. St."):
            index2 = stats_df[stats_df['Team']=="Central Connecticut"].index.values
       
        #print(row['Team_1'], ": ", index1, row['Team_2'], ": ",index2)
    
    if(index1.any() and index2.any()):
        print(row['Team_1'], ": ", index1, row['Team_2'], ": ",index2)
        #assigning the stats to the teams for the game to append them to the dataframe
        Date  = '2-2-23' #naturally this will change a lot
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
        
        compiled_df = compiled_df.append({'Date':Date, 'Team_1':Team_1, 'Team_2':Team_2, 'T1AEM':T1AEM, 'T2AEM':T2AEM, 'Team_1_Score':Team_1_Score, 'Team_2_Score':Team_2_Score,
                                          'T1AOE':T1AOE, 'T1ADE':T1ADE, 'T1AT':T1AT, 'T1Luck':T1Luck, 'T1SOSR':T1SOSR, 'T1AAOEOO':T1AAOEOO,
                                          'T1AADEOO':T1AADEOO, 'T1NCSOSR':T1NCSOSR, 'T2AOE':T2AOE, 'T2ADE':T2ADE, 'T2AT':T2AT, 'T2Luck':T2Luck,
                                          'T2SOSR':T2SOSR, 'T2AAOEOO':T2AAOEOO, 'T2AADEOO':T2AADEOO, 'T2NCSOSR':T2NCSOSR}, ignore_index=True)
#compiled_df.to_csv('compiled_stats\\cbbdata.csv', index=False)
