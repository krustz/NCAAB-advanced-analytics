#kempomScraper.py
#Cullen Wise
#created 1-31-23 edited 2-7-23
#web scraper for kenpom site
#hours burned in this file [5]

import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")#useless pandas warmsing i dont want in my precious console
#setting up urls and headers so we can access site
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
url = "https://kenpom.com/"
kempom = requests.get(url, headers=headers)
soup = BeautifulSoup(kempom.content, "html.parser")
table = soup.find(id="ratings-table")

#defining dataframe

df = pd.DataFrame(columns=['Rank', 'Team', 'Confrence', 'Win_Loss', 'Adjusted_Efficiency_Margin', 'Adjusted_Offensive_Efficency'
                           ,'Adjusted_Defensive_Efficency', 'Adjusted_tempo', 'Luck', 'Strength_of_Schedule_Rating'
                           ,'Adverage_Adjusted_Offensive_Efficency_of_Opponents','Adverage_Adjusted_Defensive_Efficency_of_Opponents',
                           'Non_Confrence_Strength_of_Schedule_Rating'])

for row in table.tbody.find_all('tr'):
    #lets get the data in the columns
   
    columns = row.find_all('td')
    if(columns != []):
        
        Rank = columns[0].text.strip()
        Team = columns[1].text.strip()
        Confrence = columns[2].text.strip()
        Win_Loss = columns[3].text.strip()
        Adjusted_Efficiency_Margin = columns[4].text.strip()
        Adjusted_Offensive_Efficency= columns[5].text.strip()
        Adjusted_Defensive_Efficency= columns[7].text.strip()
        Adjusted_tempo= columns[9].text.strip()
        Luck= columns[11].text.strip()
        Strength_of_Schedule_Rating= columns[13].text.strip()
        Adverage_Adjusted_Offensive_Efficency_of_Opponents= columns[15].text.strip()
        Adverage_Adjusted_Defensive_Efficency_of_Opponents= columns[17].text.strip()
        Non_Confrence_Strength_of_Schedule_Rating= columns[19].text.strip()
        #the spacing here was the error so df was getting appended with repetitive values when the columns were empty beause the appending of the dataframe was outside the scope of the if statement
        df = df.append({'Rank': Rank, 'Team': Team, 'Confrence': Confrence, 'Win_Loss': Win_Loss, 'Adjusted_Efficiency_Margin': Adjusted_Efficiency_Margin,
                        'Adjusted_Offensive_Efficency': Adjusted_Offensive_Efficency, 'Adjusted_Defensive_Efficency': Adjusted_Defensive_Efficency,
                        'Adjusted_tempo': Adjusted_tempo, 'Luck': Luck, 'Strength_of_Schedule_Rating':Strength_of_Schedule_Rating,
                        'Adverage_Adjusted_Offensive_Efficency_of_Opponents':Adverage_Adjusted_Offensive_Efficency_of_Opponents,
                        'Adverage_Adjusted_Defensive_Efficency_of_Opponents':Adverage_Adjusted_Defensive_Efficency_of_Opponents,
                        'Non_Confrence_Strength_of_Schedule_Rating':Non_Confrence_Strength_of_Schedule_Rating}, ignore_index=True)


#writing out to csv in .zip folder
#this piece is commented out to avoid overwriting the kenpom data for a given day
#df.to_csv('stats/stats2-7-23.csv', index=False)
