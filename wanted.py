from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from config import user_agent


def scrape_wanted(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(extra_http_headers={"User-Agent": user_agent})
    page = context.new_page()
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
    time.sleep(2)
    for _ in range(3):
        page.keyboard.down("End")
        time.sleep(0.3)
    content = page.content()
    p.stop()
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.select(".JobCard_container__REty8")
    job_info = []
    for job in jobs:
        title = job.select_one("strong").text
        company = job.select_one(".JobCard_companyName__N1YrF").text
        link = job.select_one("a")["href"]
        job_info.append(
            {
                "title": title,
                "company": company,
                "link": f"https://www.wanted.co.kr{link}",
            }
        )
    return job_info
