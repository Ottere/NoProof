import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8aa26b8b1770a6ab56db10f3dd0f3820'
redirect_uri = 'https://example.com/oauth'
authorize_code = '4q4tFP-_hvRkHSj5w-YPnhLzmrdNEwxT2iuWrHfJvlntbfbhBzS7uTNMrI6-XvLce0H9Dgo9cpgAAAF7vqXfyg'

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
#1.
# with open(r"C:/Users/user/OneDrive/바탕 화면/selenium 크로링/kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)



# # json 읽어오기
# import json
# #1.
# # with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","r") as fp:
# #     ts = json.load(fp)
# # print(ts)
# # print(ts["access_token"])

# #2.
# with open("kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])