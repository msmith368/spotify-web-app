from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# 

# Client id and secret authentication for interacting with spotify web api 
# loads envirnmnet variables from .env file
load_dotenv()

# Pull id and authenticaation tokens
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Spotify web api requires client_id and client_secret
# to be sent in a post request in order to retrieve your acces token
def get_token():
    auth_string = client_id + ":" + client_secret
    # 
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
            "Authorization" : "Basic " + auth_base64, 
            "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Used for making api calls 
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Search for an artist
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"    
    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print(json_result)

token = get_token()
search_for_artist(token,"lil durk")
