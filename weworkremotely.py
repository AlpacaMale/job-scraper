from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


def wwr(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    time.sleep(3)
    content = page.content()
    page.close()

    soup = BeautifulSoup(content, "html.parser")
    section = soup.select_one("section.jobs")
    if not section:
        return None
    jobs = section.select("article > ul > li")[:-1]
    job_info = []
    for job in jobs:
        if job.select_one(".title--ad"):
            continue
        title = job.select_one("span.title").text
        company, position, region = [obj.text for obj in job.select(".company")]
        link = job.select("a")[1]["href"]
        job_info.append(
            {
                "title": title,
                "company": company,
                "position": position,
                "region": region,
                "link": link,
            }
        )
    return job_info
