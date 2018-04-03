import pandas as pd
import json
import requests

cookies = {
    's_fid': '1233030CE039115B-0C49632FE0010CAF',
    's_cc': 'true',
    's_sq': '%5B%5BB%5D%5D',
    'ak_bmsc': '6CCC3F21E29896511AF93696E137BB36174FF00CBE4D00009BCDC25A3BB45D1F~plcZDKr7mKamhXecP/KOTiBQZuIHWIJdgGklLBHVoXLcgtCZU31k31cRu06UnvOBeWnduUAtIY7ZjG394sJoRmIEO/MkYPCy3m4m1P2c4Zl8OdwR/oiVMDlXSRiEEBVSMiXu5lXGX81jGMZwr/lJjOpykjAxKKxBZQ7r0dFy522KpLm+UQr6xIf68aDtACECHFhR5S99o+OCg7DdoSuosTwMevVOXIwsKqmMIeqN3AnUw=',
    'bm_sv': 'FACE3EC06A87668C584D3E554F1CAA13~DUNIcR0uJtHd9yxWCEJ25BlamxzmZer1HPLNEETs52U1vjRyeQIsBFXI469E1eXKnFWzehsHrUE4i8dAsoYEVMr1B03TErDMDL3G1TChC6orwIcYzzezJuyFMAuYnQbvInercoUE8M1AEhrtWbFvIA==',
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

params = (
    ('LeagueID', '00'),
    ('SeasonYear', '2017-18'),
)

response = requests.get('https://stats.nba.com/stats/draftcombineplayeranthro', headers=headers, params=params, cookies=cookies)

data = response.json()

headers = data['resultSets'][0]['headers']
playerdata = data['resultSets'][0]['rowSet']

df = pd.DataFrame(playerdata,columns=headers)
