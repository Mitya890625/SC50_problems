import json, sys, requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#print(json.dumps(response.json(), indent=2)) 
time = response.json()
usd = time['bpi']
rate = usd['USD']
rate_flt = float(rate['rate'].replace(',' , ''))
argv_flt = float(sys.argv[1])
print(rate_flt*argv_flt)
