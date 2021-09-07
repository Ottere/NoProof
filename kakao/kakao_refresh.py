import requests
import json
url = "https://kauth.kakao.com/oauth/token"
data = {
"grant_type" : "refresh_token",
"client_id" : "8aa26b8b1770a6ab56db10f3dd0f3820",
"refresh_token" : "wfsSSKjJ7-_WZXfF4t5ZJTFhInIZE-vRTtiqeQo9cpcAAAF7qSnHJg"
}
response = requests.post(url, data=data)
tokens = response.json()
# print(response.json())

with open("kakao_code.json","w") as fp:
json.dump(tokens, fp)