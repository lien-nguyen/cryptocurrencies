from  lib import getData 
from lib import credentials
import os

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
api_key = credentials.api_tokens 

data = getData.get_data(url, api_key)


