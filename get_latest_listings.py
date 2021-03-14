from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, codecs

import os

os.system("mkdir data") # Create a folder data that will store scrapped data

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '87c8f939-6ef3-44f0-863c-c07a7d3df545',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  with open('data.json', 'wb') as f:
    os.system("mv data.json data/") # Move scrapped data to the folder data
    json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

