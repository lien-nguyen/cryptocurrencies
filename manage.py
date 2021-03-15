from  lib import getData 
from lib import config 
import os


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
api_key = config.api_tokens 

data = getData.get_data(url, api_key) # the api_key is store in the credentials.py, replace your api key with your own


