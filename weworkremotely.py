import requests
from bs4 import BeautifulSoup

all_jobs = []


def scrape_wwr(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )
    jobs = soup.find("section", class_="jobs").find_all("li")[1:]
    for job in jobs:
        title_data = job.find("span", class_="title")
        if title_data == None:
            continue
        title = title_data.text
        company, position, region = (
            company.text for company in job.find_all("span", class_="company")
        )
        link = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "link": f"https://weworkremotely.com{link}",
        }
        all_jobs.append(job_data)
    return all_jobs[0]
