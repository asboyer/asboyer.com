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

# favorites

# music
@app.route("/music")
def music():
    return render_template("favorites/music/music.html")

@app.route("/music/current")
def music_current():
    return render_template("favorites/music/current.html")

@app.route("/music/all-time")
def music_all():
    return render_template("favorites/music/all-time.html")