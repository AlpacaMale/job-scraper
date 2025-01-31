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


def scrape_wwr(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    time.sleep(2)
    content = page.content()
    p.stop()

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
                "link": f"https://weworkremotely.com{link}",
            }
        )
    return job_info
