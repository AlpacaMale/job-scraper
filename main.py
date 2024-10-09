from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

keywords = ["flutter", "golang", "python"]
keyword = keywords[0]

url = f"https://remoteok.com/remote-{keyword}-jobs"

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto(url)
time.sleep(2)
content = page.content()
p.stop()
soup = BeautifulSoup(content, "html.parser")
jobs = soup.find("tbody").find_all("tr", class_="job")
all_jobs = []
for job in jobs:
    title = job.find("h2", itemprop="title").text.strip()
    company = job.find("h3", itemprop="name").text.strip()
    position = ",".join(
        position.text.strip()
        for position in job.find("td", class_="tags").find_all("h3")
    )
    region_datas = job.find_all("div", class_="location")
    region = region_datas[0].text if len(region_datas) == 2 else ""
    link = f"https://remoteok.com{job.find('a',class_='preventLink')['href']}"
    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "link": link,
    }
    all_jobs.append(job_data)

print(all_jobs)
