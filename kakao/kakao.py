import requests

url = 'https://kauth.kakao.com/oauth/token' # 카카오 api 서버에 요청할 url 주소
rest_api_key = '8aa26b8b1770a6ab56db10f3dd0f3820' # 본인 앱의 REST API 키 값
redirect_uri = 'https://example.com/oauth' # 본인 앱의 Redirect_Uri
authorize_code = '4q4tFP-_hvRkHSj5w-YPnhLzmrdNEwxT2iuWrHfJvlntbfbhBzS7uTNMrI6-XvLce0H9Dgo9cpgAAAF7vqXfyg' # 본인 앱의 인가코드 (모를경우 github kakao 폴더 내의 md 파일 참고)

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data) # 카카오 서버에 post 형식으로 데이터 전송
tokens = response.json() # 카카오 서버에서 받은 데이터를 json 형태로 tokens에 저장
print(tokens)

# json 저장
import json
#1.
# with open(r"C:/Users/user/OneDrive/바탕 화면/selenium 크로링/kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp: #현재 디렉토리에 kakao_code.json이란 파일을 쓰기 모드로 오픈 (없으면 생성)
    json.dump(tokens, fp) # tokens을 오픈한 json 파일에 입력

#-----------------------------------------------------------------------------------------------------

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