from decouple import config
from requests_oauthlib import OAuth1Session


API_KEY = config('API_KEY')
API_SECRET_KEY = config('API_SECRET_KEY') 
ACCESS_TOKEN = config('ACCESS_TOKEN') 
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET') 

twitter = OAuth1Session(
   API_KEY,
   API_SECRET_KEY,
   ACCESS_TOKEN,
   ACCESS_TOKEN_SECRET
)
