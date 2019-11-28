from decouple import config
from requests_oauthlib import OAuth1Session


API_KEY = config('API_KEY')
API_SECRET_KEY = config('API_SECRET_KEY') 
ACCESS_TOKEN = config('ACCESS_TOKEN') 
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET') 

def get_auth():
   twitter_auth = OAuth1Session(
      API_KEY,
      API_SECRET_KEY,
      ACCESS_TOKEN,
      ACCESS_TOKEN_SECRET
   )

   return twitter_auth
