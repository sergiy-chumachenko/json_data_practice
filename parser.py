import json
from urllib.request import urlopen
from pprint import pprint

# Using https://currencylayer.com
# access_key = '{your access key}'
access_key = 'access_key=your_access_key'
currencies = 'currencies=EUR,GBP,CAD,PLN'
source = 'source=USD'
format = 'format=1'
with urlopen("http://apilayer.net/api/live" + '?' + access_key + '&' + currencies + '&' + source + '&' + format) \
        as response:
    source = response.read()
data = json.loads(source)
pprint(json.dumps(data, indent=2))

usd_rates = dict()
for item in data['quotes']:
    name = item
    price = data['quotes'][str(item)]
    usd_rates[name] = price

pprint(50 * usd_rates['USDEUR'])