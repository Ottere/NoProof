# selenium
분당경영고등학교 python 2팀  
  
  #### _python selenium을 이용해 국세청 홈택스의 데이터를 크롤링하고  flask 웹서버와 연결하여 웹 화면에 나타내기_

질문사항 및 개선사항 또는 변경할 부분은 언제든지 단체톡방에서 물어보길 바랍니다.  
(컴퓨터 앞에만 있다면 업무시간 외에도 답변가능)


## pip install
시작하기 앞서 프로그램 실행에 필요한 모듈을 설치하겠습니다.  
이후의 모든 설정은 터미널창에서 실행됩니다. (VSCODE에서 Ctrl + ` 누르면 바로 터미널 창이 열립니다.)

  
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
   + 추가 사항) .schema 명령어를 이용하면 테이블과 테이블 내부의 컬럼과 데이터타입까지 확인이 가능합니다  
4. 실제 생성하기
   >  create table tblErpTaxBillTrans(  
      TransSeq int PRIMARY KEY,  
      FromSaupjaRegNo text,  
      FromSaupjangNo text,  
      FromSaupjaname text,  
      FromDaepyoName text,  
      FromSaupjangAd text,  
      FromUptae text text,  
      FromJongmok text,  
      FromEmailAddr1 text,  
      ToSaupjaRegNo text,  
      ToSaupjangNo text,  
      ToSaupjaName text,  
      ToDaepyoName text,  
      ToSaupjangAddr text,  
      ToUptae text,  
      ToJongmok text,  
      ToEmailAddr1 text,  
      ToEmailAddr2 text,  
      HomeTaxApprNo text,  
      RegDate text,  
      AmtUnc text,  
      AmtTax text,  
      EditSayoo text,  
      AmtTot text,  
      AmtCash text,  
      AmtSupyo text,  
      AmtUEum text,  
      AmtMisu text,  
      GubunRequPay text,  
      FlowProcYN text,  
      SyncIndex text,  
      CorpCode text);

## 실제 실행하기
+ 현재 레포지토리에 있는 static 폴더, templates폴더 , crawling.py, sqlite3, chromedriver를 다운받기  
  (chromedriver의 경우 각자 크롬에 맞게 다운로드 바랍니다. github에 올라가 있는 버전은 92.0.4515.159 버전 입니다.)
+ 카카오톡으로 보내준 공인인증서 컴퓨터로 다운받아 브라우저에 저장하기  
  (직접 한번 로그인까지 실행해서 공인인증서를 인식시켜야합니다.)
+ 터미널 입력창에 python [파일이름].py (crawling.py) 입력 
+ 인터넷 주소칸에 127.0.0.1/ 입력후 이동 (여기까지 오면 메인 화면이 보임)
+ 127.0.0.1/crawling 주소로 이동하면 selenium이 실행되며 크롤링 진행이됩니다.
