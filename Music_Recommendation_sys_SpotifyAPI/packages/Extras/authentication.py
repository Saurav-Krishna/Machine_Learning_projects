# creaing authentication 

import requests
import base64

client_id = '002c40613a6c4139a82df6838816476e'
client_secret = '9ed39f8050cc4b3e88449283d8ad4edb'

# base64 for encoding
client_credentials = f'{client_id}:{client_secret}'
client_credentials_base64 = base64.b64decode(client_credentials.encode('latin-1')).decode('latin-1')

# Request the access token

token_url = 'https://accounts.spotify.com/en-GB/status?flow_ctx=9aebfbd1-2140-4e47-9195-1a51839af9d6%3A1701663841/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64}'
}
data = {
    'grant_type': 'client_credentials'
}
response = requests.post(token_url,data=data,headers = headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully")
else:
    print("Error obtaining access token.")
    exit()

