from flask import Flask, render_template, request
from remoteok import scrape_remoteok
from weworkremotely import scrape_wwr

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("index.html", name="nico")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    wwr = scrape_wwr(keyword)
    remote = scrape_remoteok(keyword)
    jobs = wwr + remote
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run(debug=True)
