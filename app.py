from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<page>")
def main_page(page):
    if os.path.exists(f'templates/{page}.html'):
        return render_template(f'{page}.html')
    else:
        return render_template("error.html")

@app.route("/press")
def press():
    return render_template("about/news.html")

# blogs

@app.route("/blog")
def blog():
    return render_template("blog/blog.html")

@app.route("/blog/<name>")
def blog_post(name):
    if os.path.exists(f'templates/blog/{name}.html'):
        # return render_template(f"blog/{name}.html")
        return render_template(f"soon.html")
    else:
        # make error page
        return render_template("error.html")

# favorites

# music
@app.route("/music")
def music():
    return render_template("favorites/music/music.html")

@app.route("/music/<name>")
def music_path(name):
    if os.path.exists(f'templates/favorites/music/{name}.html'):
        return render_template(f"favorites/music/{name}.html")
    else:
        # make error page
        return render_template("error.html")


# movies
@app.route("/movies")
def movies():
    return render_template("favorites/movies/movies.html")

# archives


@app.route("/archive/music/0")
def music_archive_0():
    return render_template("archive/music/april-june-2021.html")

@app.route("/archive/music/1")
def music_archive_1():
    return render_template("archive/music/july-2021.html")

@app.route("/archive/music/<name>")
def archive_music_path(name):
    if os.path.exists(f'templates/archive/music/{name}.html'):
        return render_template(f"archive/blog/{name}.html")
    else:
        # make error page
        return render_template("error.html")

# @app.route("/books")
# def books():
#     return render_template("favorites/books/books.html")

# @app.route("/books/<name>")
# def book_path(name):
#     if os.path.exists(f'templates/favorites/books/{name}.html'):
#         return render_template(f"favorites/books/{name}.html")
#     else:
#         # make error page
#         return render_template("error.html")

# @app.route("/books/shelf")
# def books_shelf():
#     return render_template("favorites/books/bookshelf.html")

# # shelf

# @app.route("/books/shelf/<name>")
# def book_shelf_path(name):
#     if os.path.exists(f'templates/favorites/books/shelf/{name}.html'):
#         return render_template(f"favorites/books/shelf/{name}.html")
#     else:
#         # make error page
#         return render_template("error.html")

# @app.route("/books/library")
# def books_library():
#     return render_template("favorites/books/library.html")

#SEO
@app.route("/robots.txt")
def se1():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def se2():
    return send_from_directory(app.root_path, "sitemap.xml")
