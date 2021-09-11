# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
import json
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql.elements import Null
from werkzeug.utils import secure_filename
import os, sys, re
import random, string
import pymysql
import sqlalchemy 
from itertools import groupby
import time, win32con, win32api, win32gui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from urllib.request import urlretrieve

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

app = Flask(__name__)
app.secret_key = "Secret Keyf"
# 이곳에서 sqlite3 연결
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///craw.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

options=webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080') 
options.add_argument("disable-gpu")
options.add_argument("user-data-dir=C:\\environments\\selenium")
# chrome 드라이버 chrome 버전에 맞게 다운후 위치변경
driver = webdriver.Chrome('chromedriver.exe', options=options) #또는 chromedriver.exe
driver.maximize_window()
actions = webdriver.ActionChains(driver)
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

hometex='https://comic.naver.com/webtoon/weekday'
driver.get(hometex)

#비활성화 된 카톡창 이름
kakao_opentalk_name = '동화'


def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

#메인 카톡창 지정
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
#메인창에서 텍스트 박스지정(RICHEDIT50W)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

time.sleep(3)
for i in range(1,51):
 webtext=driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div/ul/li['+str(i)+']/a').text
 time.sleep(0.2)
 kakao_sendtext(webtext)
