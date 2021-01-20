# ------------------------------------------
# python = 3.7.3
# python의 venv 모듈을 이용하여 가상환경 생성
#
# 설치한 패키지
# bs4==0.0.1
# requests==2.25.1
# -------------------------------------------

import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')

pages = []
# pagination의 page 번호 가져옴
# int 로 형변환 하는 과정에서 next에 대한 형변환 오류를 방지하기 위해 마지막 내용 slicing
for link in links[:-1]:
    pages.append(int(link.string))
max_page = pages[-1]
