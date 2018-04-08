import requests
import time
import pandas as pd
import json
  
#change url depending on what stats you want to pull
url = 'https://stats.nba.com/stats/draftcombineplayeranthro'

d = {}

#Change cookies and headers to yours by going to the stats.nba.com page, getting the cURL information,
#and converting them to python using https://curl.trillworks.com/
cookies = {
}

headers = {
}

#change loop iterations for looping over many sets of data
for i in range(0,17):

    #here we pull the data for the 2000-2017 seasons - change season in loop to pull other data
    if i < 10:
        season = '200'+str(i)+'-0'+str(i+1)
        if i == 9:
            season = '200'+str(i)+'-'+str(i+1)
    if i > 9:
        season = '20'+str(i)+'-'+str(i+1)
        
    params = (
        ('LeagueID', '00'),
        ('SeasonYear', season),
    )
    
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    data = response.json()
    heads = data['resultSets'][0]['headers']
    playerdata = data['resultSets'][0]['rowSet']
    df = pd.DataFrame(playerdata,columns=heads)
    d[i] = df
    #very important for stats.nba.com. Without a delay they will block your IP if you're pulling many sets.
    time.sleep(5)

df_all = pd.concat(d.values())
#change output file depending on what you scraped
df_all.to_csv('playercombine00_17.csv', encoding='utf-8', index=False)
