import requests
import time
import pandas as pd
import json
  
#change url depending on what stats you want to pull
url = 'https://stats.nba.com/stats/draftcombineplayeranthro'

d = {}

#These are my default cookies and headers. Change those to yours by going to the stats.nba.com page, getting the cURL information,
#and converting them to python using https://curl.trillworks.com/
cookies = {
    's_fid': '1233030CE039115B-0C49632FE0010CAF',
    's_cc': 'true',
    'ak_bmsc': '8827018A8BA6595B96394EAEB8EDE99CB81C7F0D902A0000EE2CC45A6B0E8A0C~pl+p4bUAp8heShFsu82vtWedpDqQG87TZEwOCWzKKiio/ke5Sh2BQZ9U0NeUg0hYZEixSRvU1WFj0iPCbbOtYgoaKuZBKgpAFC0kSQId9ngnX0Nw3cWAaYj8Bp+C8Eg2VWKK+2ahh1jxFZPICYDoGYHg6AU1KTIBSG7Hfkcb3XGX1Jk2imVlwyQZB+doB/kGLAwjr3rMxcbLkyJ9INCfv6Xj2NmkQFOfUtJwlUhcnWoMM=',
    'bm_sv': '69BF11E05DF055FD346C24D847ACDE2D~NCcZj34qsofDCTEzz7QZT0aPLc/Z8VIRY4gcH5jY6/fDQ+Yy2Kdl94icGSugAeDjtBpjpfL4u7uDkmQBGVfILxmqe+s2oWFBRKCMgTpwLBD0oZFXeYsZYC1f4E6eQXn+KB36LZP0RJ5dY8lYOhMAKQ==',
    's_sq': 'nbag-n-league%3D%2526pid%253Dstats.nba.com%25253A%25252Fdraft%25252Fcombine-spot-up%25252F%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fstats.nba.com%25252Fdraft%25252Fcombine-anthro%25252F%2526ot%253DA',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.nba.com/draft/combine-anthro/',
    'Connection': 'keep-alive',
    'x-nba-stats-origin': 'stats',
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
