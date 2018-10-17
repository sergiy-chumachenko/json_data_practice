import json
from urllib.request import urlopen

# Using https://currencylayer.com
access_key = '{your access key}'
currencies = 'currencies=EUR,GBP,CAD,PLN'
source = 'source=USD'
format = 'format=1'
with urlopen("http://apilayer.net/api/live" + '?' + access_key + '&' + currencies + '&' + source + '&' + format) as response:
    source = response.read()
print(source)