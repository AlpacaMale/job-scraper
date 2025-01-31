from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


def scrape_remoteok(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    time.sleep(2)
    content = page.content()
    p.stop()
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.select("table#jobsboard > tbody > tr.job")
    job_info = []
    for job in jobs:
        title = job.select_one("h2[itemprop='title']").text.strip()
        company = job.select_one("h3[itemprop='name']").text.strip()
        position = ", ".join(tag.text.strip() for tag in job.select(".tag > h3"))
        region_data = job.select(".location")[:-1]
        region = region_data[0].text if region_data else ""
        link = job.select_one("a")["href"]
        job_info.append(
            {
                "title": title,
                "company": company,
                "position": position,
                "region": region,
                "link": f"https://remoteok.com{link}",
            }
        )
    return job_info
