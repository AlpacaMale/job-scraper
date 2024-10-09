from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


class WantedScraper:
    def __init__(self, terms):
        self.terms = terms

    def scrape_page(self):
        for term in self.terms:
            p = sync_playwright().start()
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(f"https://www.wanted.co.kr/search?query={term}&tab=position")
            time.sleep(1.5)
            # page.click("button.Aside_searchButton__rajGo")
            # time.sleep(0.1)
            # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
            # time.sleep(0.1)
            # page.keyboard.down("Enter")
            # time.sleep(0.5)
            # page.click("#search_tab_position")
            # time.sleep(0.5)
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
                reward = job.find("span", class_="JobCard_reward__cNlG5").text
                job = {
                    "title": title,
                    "company": company,
                    "reward": reward,
                    "link": link,
                }
                all_jobs.append(job)

            file = open(f"{term} jobs.csv", "w")
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Title",
                    "Company",
                    "Reward",
                    "Link",
                ]
            )
            for job in all_jobs:
                writer.writerow(job.values())
            file.close()

    def show_terms(self):
        print(", ".join(self.terms))

    def add_terms(self, term):
        self.terms.append(term)

    def remove_terms(self, term):
        try:
            self.terms.remove(term)
        except:
            print("값이 없습니다.")


scraper = WantedScraper(["flutter", "kotlin", "python"])
scraper.show_terms()
scraper.scrape_page()
