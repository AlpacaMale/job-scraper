from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


def scrape_wanted(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
    time.sleep(2)
    for _ in range(3):
        page.keyboard.down("End")
        time.sleep(0.3)
    content = page.content()
    p.stop()
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__REty8")
    all_jobs = []
    for job in jobs:
        link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__HBpZf").text
        company = job.find("span", class_="JobCard_companyName__N1YrF").text
        job = {
            "title": title,
            "company": company,
            "link": link,
        }
        all_jobs.append(job)
    return all_jobs
