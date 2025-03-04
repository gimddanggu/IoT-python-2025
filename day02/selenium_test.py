# 버전확인
'''import selenium
print(selenium.__version__)'''


# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 크롬드라이버 실행
driver = webdriver.Chrome(options=chrome_options) 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://finance.naver.com/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)
