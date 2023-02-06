#CollegebbScraper.py
#Cullen Wise
#2-2-23
#scrapes sports teams and scores

import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")#useless pandas warmsing i dont want in my precious console

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
url = 'https://www.ncaa.com/scoreboard/basketball-men/d1/2023/02/01/all-conf'
#url = 'https://www.ncaa.com/scoreboard/basketball-men/d1/2023/01/31/all-conf'
scores_page = requests.get(url, headers=headers)

soup = BeautifulSoup(scores_page.content, "html.parser")
#going into the general area on the page we want

df = pd.DataFrame(columns=['Team_1', 'Team_2', 'Team_1_Score', 'Team_2_Score'])



#putting all the values wanted into a dataframe
    
names = soup.find_all(class_="gamePod-game-team-name")
scores = soup.find_all(class_="gamePod-game-team-score")
#were going to force this to iterate through every game on the page
try:
    for i in range(181):#181 is the max theorhetical mens D1 cbb games that could be played
        
        #index is the way it is due to teams in games being grouped together in the tables
        Team_1 = names[2*i].text.strip()
        Team_2 = names[(2*i)+1].text.strip()
        Team_1_Score = scores[2*i].text.strip()
        Team_2_Score = scores[(2*i)+1].text.strip()
        print(Team_1, ": ", Team_1_Score," VS ",Team_2, ": ", Team_2_Score)
        #add files to data frame 
        df = df.append({'Team_1':Team_1, 'Team_2':Team_2, 'Team_1_Score':Team_1_Score, 'Team_2_Score':Team_2_Score}, ignore_index=True)

except IndexError:
    print("index out of B 0 u N D Z")
    
#df.to_csv('games/scores1-31-23.csv', index=False)
df.to_csv('games/scores2-1-23.csv', index=False)
