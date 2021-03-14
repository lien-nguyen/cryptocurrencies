from  lib import getData 
import os

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
data = getData.get_data(url)


