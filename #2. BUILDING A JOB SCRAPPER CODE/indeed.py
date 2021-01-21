import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []
    # pagination의 page 번호 가져옴
    # int 로 형변환 하는 과정에서 next에 대한 형변환 오류를 방지하기 위해 마지막 내용 slicing
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        title = result.find("h2", {"class": "title"}).find("a")["title"]

    return jobs
