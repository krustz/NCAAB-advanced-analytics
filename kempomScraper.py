#Kempom scraper
#Cullen Wise
#1-31-23
#web scraper

#import beautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulSoup
#https://kenpom.com/

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
url = "https://kenpom.com/"
kempom = requests.get(url, headers=headers)

#print(kempom.text) we dont need to print that lmao


soup = BeautifulSoup(kempom.content, "html.parser")
#table id=ratings-table we want this 
table = soup.find(id="ratings-table")
#print(results.prettify())

#define dataframe

df = pd.DataFrame(columns=['Rank', 'Team', 'Confrence', 'Win_Loss', 'Adjusted_Efficiency_Margin', 'Adjusted_Offensive_Efficency'
                           ,'Adjusted_Defensive_Efficency', 'Adjusted_tempo', 'Luck', 'Strength_of_Schedule_Rating'
                           ,'Adverage_Adjusted_Offensive_Efficency_of_Opponents','Adverage_Adjusted_Defensive_Efficency_of_Opponents',
                           'Non_Confrence_Strength_of_Schedule_Rating'])
#13 columns
for row in table.tbody.find_all('tr'):
    #lets get the data in the columns
    
    columns = row.find_all('td')
    if(columns != []):
        #mod 21 maybe
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

    df = df.append({'Rank': Rank, 'Team': Team, 'Confrence': Confrence, 'Win_Loss': Win_Loss, 'Adjusted_Efficiency_Margin': Adjusted_Efficiency_Margin,
                    'Adjusted_Offensive_Efficency': Adjusted_Offensive_Efficency, 'Adjusted_Defensive_Efficency': Adjusted_Defensive_Efficency,
                    'Adjusted_tempo': Adjusted_tempo, 'Luck': Luck, 'Strength_of_Schedule_Rating':Strength_of_Schedule_Rating,
                    'Adverage_Adjusted_Offensive_Efficency_of_Opponents':Adverage_Adjusted_Offensive_Efficency_of_Opponents,
                    'Adverage_Adjusted_Defensive_Efficency_of_Opponents':Adverage_Adjusted_Defensive_Efficency_of_Opponents,
                    'Non_Confrence_Strength_of_Schedule_Rating':Non_Confrence_Strength_of_Schedule_Rating}, ignore_index=True)
#df = df.append({'Rank': Rank, 'Team': Team, 'Confrence': Confrence, 'Win_Loss': Win_Loss}, ignore_index=True)
print(df.head())
compression_opts = dict(method='zip',archive_name='out.csv')  

df.to_csv('out.zip', index=False,compression=compression_opts)
