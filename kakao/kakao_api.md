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
+ 좌측에 동의항목으로 이동하신 이후 닉네임 - 필수동의, 카카오톡 메시지 전송 - 선택동의로 설정하시고 동의 목적은 아무렇게나 쓰셔도 됩니다.  

## 인증 코드 받기
    카카오 제공 REST API 문서 위치 : 우측 상단 문서 > 카카오 로그인 > REST API > 인가 코드 받기
https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code
+ 위 URL 주소가 인가 코드를 받아오는 주소입니다.
+ {REST_API_KEY}와 {REDIRECT_URL}에는 본인의 REST API키 그리고 REDRIECT_URL값을 넣어줍니다.
+ ex) https://kauth.kakao.com/oauth/authorize?client_id=e294f98ad14180062a8fefd60bf70274&redirect_uri=https://example.com/oauth&response_type=code
+ *카카오 로그인을 해야하므로 크롬에서 Ctrl+Shift+N을 눌러 시크릿 모드로 열어줍니다. (직접 다른방법으로 열어도 상관없음)
+ URL을 입력하여 이동시 카카오 로그인이 뜨고 로그인 이후 
![image](https://user-images.githubusercontent.com/69878816/132789530-97a76bf4-0e55-469c-a754-f794cb9dae62.png)
+ 해당 화면이 나오면 성공, 해당 화면 URL의 ?code=의 뒤부터 복사하여 저장합니다. 
+ ex) tIQ9GMdfOCFKQFqpAwfwASAjbnbxRQj_2Zmqlj8RzpTCO5z1aHaJpz2RCLqSul1tEbBw-Qo9dZoAAAF7zYi9Ww
