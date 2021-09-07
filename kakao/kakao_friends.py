import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8aa26b8b1770a6ab56db10f3dd0f3820'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'Y3-85uvSfQac2ZcSC935oWM2QPj8g9kyj9Ht1kQdZ8CWuNq8L-XZCJvkom1eOC0haWGk9Ao9dGkAAAF7uLfnuw'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open("kakao_friends_code.json","w") as fp:
    json.dump(tokens, fp)