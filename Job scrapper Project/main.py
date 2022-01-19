# ------------------------------------------
# python = 3.7.3
# python의 venv 모듈을 이용하여 가상환경 생성
#
# 설치한 패키지
# bs4==0.0.1
# requests==2.25.1
# -------------------------------------------

from indeed import extract_indeed_pages, extract_indeed_jobs
from save import save_to_file

last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)
# save_to_file()
