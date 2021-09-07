import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '6ae276f9f771f2e43af49ff089efebe9'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'hw1YwGkzk1cguw2bB9OcnwNKVzo-fRK3V_NQzwCnYaT_QiocpW5mesK6vFrh-JOyaLuPsgo9c-wAAAF7vg3CMQ'

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
with open("kakao_friends_code_test.json","w") as fp:
    json.dump(tokens, fp)