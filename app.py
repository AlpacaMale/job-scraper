from flask import Flask, render_template, request, redirect, send_file
from scraper import scrape_remoteok, scrape_wanted, scrape_wwr
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("index.html", name="nico")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = scrape_wwr(keyword)
        remote = scrape_remoteok(keyword)
        wanted = scrape_wanted(keyword)
        jobs = wwr + remote + wanted
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run(debug=True)
