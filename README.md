# selenium
분당경영고등학교 python 2팀  
  
  #### _python selenium을 이용해 국세청 홈택스의 데이터를 크롤링하고  flask 웹서버와 연결하여 웹 화면에 나타내기_

질문사항은 언제든지 단체톡방에서 물어보길 바랍니다.  
(컴퓨터 앞에만 있다면 업무시간 외에도 답변가능)


## pip install
시작하기 앞서 프로그램 실행에 필요한 모듈을 설치하겠습니다.
  
  
  > pip install flask  
  pip install sqlalchemy  
  pip install flask-sqlalchemy  
  pip install selenium  
  pip install pymysql 
  
이로써 필요한 모듈은 모두 설치가 끝났습니다.

## DataBase
다음으로는 데이터베이스를 설치 및 구축하도록 하겠습니다.

(sql query문.txt 파일로 가면 사용한 문법이 적혀있습니다. 추가적인 내용이므로 참고하면 좋지만 하위 설명만 보고 진행해도 무관합니다.)

1. 데이터베이스 설치  
   + 데이터베이스 파일은 sqlite3.exe파일을 다운받으신 뒤 사용하실 폴더에 저장하면 됩니다

2. 데이터베이스 생성  
   
   + sqlite3.exe가 있는 폴더의 터미널 (VSCODE에서 Ctrl+` 하면 바로 열림)에서  
   ./sqlite3 [DB이름.db]하면 해당 데이터 베이스가 폴더에 생성됩니다.
   + ex) 분당경영고등학교python2팀\selenium> ./sqlite3 crawling.db
   + 위와 같이 하면 해당 selenium 폴더 안에 crawling.db라는 데이터베이스 파일이 생성됩니다.
   + 터미널 입력창이 sqlite> 로 바뀐걸 확인합니다. (이후 DB작업은 sqlite>안에서 해야하므로 필수)
3. 테이블 생성  
   + create table [테이블이름] (컬럼명1 데이터타입, 컬럼명2 데이터타입, ...);
   + ex) create table crawling (TransSeq integer PRIMARY KEY, FromSaupjaRegNo text, ...);
   + 위와 같은 방식으로 테이블 생성 이후 .tables 명령어로 테이블 목록 확인이 가능합니다. 제대로 생성됬는지 확인해보세요.
   + 추가 사항) .schema 명령어를 이용하면 테이블과 테이블 내부의 컬럼과 데이터타입까지 확인이 가능합니다.

   


