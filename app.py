from flask import Flask, render_template, request
from 

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("index.html", name="nico")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)


app.run(debug=True)
