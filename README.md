# Job Scraper

검색한 키워드를 바탕으로 3곳의 사이트를 스크래핑하여 사용자에게 제공합니다.

## 사용 모듈

- **Flask**: 경량 웹 프레임워크로, 특정 URL 경로를 함수와 매핑합니다.
- **Playwright**: 브라우저 자동화 도구로, 동적 컨텐츠를 스크래핑할 때 사용되었습니다.
- **Time**: Python의 내장 모듈로, 동적 컨텐츠가 로드될 때까지 프로그램을 대기시키는 기능으로 사용되었습니다.
- **BeautifulSoup**: 강력한 파싱 기능을 제공하는 라이브러리로, HTML 구문을 분석하여 데이터를 추출할 때 사용되었습니다.
- **os**: 운영체제와 상호작용하는 Python의 내장 모듈로, 디렉토리를 생성할 때 사용되었습니다.
- **csv**: CSV 파일을 읽고 쓰기 위한 Python의 내장 모듈로, 데이터를 CSV 형식으로 저장할 때 사용되었습니다.

## 패키지 구조

```
├── 📁 data / Directory for csv files
├── 📁 templates / Directory for HTML templates
│   └── index.html / Web entry point
├── app.py / Main entry point for Flask application
├── scraper.py / Functions for web scraping
├── file.py / Functions for saving data to files
├── config.py / Configurations settings
├── requirements.txt / List of package dependencies
└── README.md / Project documentation
```

## 실행 방법

1. **Clone repository**

```
git clone https://github.com/AlpacaMale/job-scraper
```

2. **Change directory**

```
cd job-scraper
```

3. **Install dependency**

```
pip install -r requirements.txt
```

4. **Run main.py**

```
python app.py
```
