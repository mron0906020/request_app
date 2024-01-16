import requests
from views import city

def get_wether():
   endpoint="https://weather.tsukumijima.net/api/forecast"
   params={"city":city}
   respons=requests.get(endpoint,params=params)
# dict_deta=respons.json()
# print(dict_deta["forecasts"][0]["date"]+dict_deta["forecasts"][0]["telop"])
# print(dict_deta["forecasts"][0]["temperature"]["max"]["celsius"])
