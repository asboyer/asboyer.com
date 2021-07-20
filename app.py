from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soon")
def soon():
    return render_template("soon.html")

@app.route("/press")
def news():
    return render_template("about/news.html")

# blogs
@app.route("/blog/goatgrade")
def blog():
    return render_template("blog/goatgrade.html")