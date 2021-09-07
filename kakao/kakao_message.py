import requests
import json

#1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","r") as fp:
#     tokens = json.load(fp)

#2.
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)
# https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
# "https://kapi.kakao.com/v2/api/talk/memo/default/send"
url="https://kapi.kakao.com/v2/api/talk/memo/default/send"



# 사용자 토큰
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

# data={
#     "template_id" : {'60954'},
#     "template_args" : '{"title": "제목" , "describe" : "설명"}'

# }

# response = requests.post(url, headers=headers, data=data)
# response.status_code

# data={
#     "template_object": json.dumps({
#         "object_type":"text",
#         "text":"방금, 신용카드가 결재되었습니다.",
#         "link":{
#             "web_url":"www.naver.com"
#         }
#     })
# }

template = {
    "object_type": "feed",
        "content": {
            "title": "디저트 사진",
            "description": "아메리카노, 빵, 케익",
            "image_url": "http://mud-kage.kakao.co.kr/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
            "image_width": 640,
            "image_height": 640,
            "link": {
            "web_url": "http://www.daum.net",
            "mobile_web_url": "http://m.daum.net",
            "android_execution_params": "contentId=100",
            "ios_execution_params": "contentId=100"
            }
        },
        "social": {
            "like_count": 100,
            "comment_count": 200,
            "shared_count": 300,
            "view_count": 400,
            "subscriber_count": 500
        },
        "buttons": [
            {
            "title": "웹으로 이동",
            "link": {
                "web_url": "http://www.daum.net",
                "mobile_web_url": "http://m.daum.net"
            }
            },
            {
            "title": "앱으로 이동",
            "link": {
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
            }
        ]
    }

data = {
    # "template_object" : json.dumps(template)
    'template_id': '60954'
}



response = requests.post(url, headers=headers, data=data)
print(response.status_code)

if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))