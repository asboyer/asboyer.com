from flask import Flask, render_template, send_from_directory
import os

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

@app.route("/blog")
def blog():
    return render_template("blog/blog.html")

@app.route("/blog/<name>")
def blog_post(name):
    if os.path.exists(f'templates/blog/{name}.html'):
        return render_template(f"blog/{name}.html")
    else:
        # make error page
        return render_template("blog/blog.html")

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

# movies
@app.route("/movies")
def movies():
    return render_template("favorites/movies/movies.html")

# books
@app.route("/books")
def books():
    return render_template("favorites/books/books.html")

@app.route("/books/shelf")
def books_shelf():
    return render_template("favorites/books/bookshelf.html")

# shelf

@app.route("/books/shelf/atomic-habits")
def books_shelf_atomic_habits():
    return render_template("favorites/books/shelf/atomic-habits.html")

@app.route("/books/library")
def books_library():
    return render_template("favorites/books/library.html")

#SEO
@app.route("/robots.txt")
def se1():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def se2():
    return send_from_directory(app.root_path, "sitemap.xml")