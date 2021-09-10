# 카카오 api 사용하기
    참고: https://novice-engineers.tistory.com/9?category=908185

## 카카오 디벨로퍼 가입하기 (로그인)
![image](https://user-images.githubusercontent.com/69878816/132783653-8b933c8c-a128-4809-8c2a-a609bcfc6a90.png)  

## 애플리케이션 만들기 
![image](https://user-images.githubusercontent.com/69878816/132784763-2f479b79-8ada-4201-9c98-ab046f690857.png)
+ 애플리케이션 추가하기 > 앱 이름과 사업자 명은 마음대로 해도 됩니다.

## 앱 설정
![image](https://user-images.githubusercontent.com/69878816/132787119-7d016d0a-cdc2-478a-a5ef-f019d6597d2d.png)
+ 우선 요약 정보의 REST API 키를 따로 저장해두거나 복사 해둡니다. (자주 사용됨)
![image](https://user-images.githubusercontent.com/69878816/132787320-d8c31a92-a243-4ee5-9487-4b2559e08c08.png)
+ 이후 카카오 로그인으로 이동하여 상태를 OFF -> ON으로 바꿔줍니다.
+ Redirect URI는 테스트 이므로 https://example.com/oauth 로 설정하겠습니다.
![image](https://user-images.githubusercontent.com/69878816/132787466-1ae22d8b-f969-4218-aefd-f7f2e61d27df.png)
+ 우측에 동의항목으로 이동하신 이후 닉네임 - 필수동의, 카카오톡 메시지 전송 - 선택동의로 설정하시고 동의 목적은 아무렇게나 쓰셔도 됩니다.
