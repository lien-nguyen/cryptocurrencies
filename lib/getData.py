from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, codecs

import os


def get_data(url, api_key):

  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    with open('data.json', 'wb') as f:
      json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
      os.system("mkdir data") # Create folder data that will hold scrapped data
      os.system("mv data.json data/") # Move scrapped data to the folder data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  
  return data

