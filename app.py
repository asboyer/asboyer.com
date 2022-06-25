import os
import json
import inflect
import smtplib
import re
import requests

from flask import Flask, render_template, send_from_directory, redirect, url_for
from datetime import date
from datetime import datetime
from pytz import timezone
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from secret import secret_key, EMAIL_ADDRESS, EMAIL_PASS

grade = "senior"
school = "Wayland High School"

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age

birthday = date(2003, 9, 21)
p = inflect.engine()

age_string = p.number_to_words(calculateAge(birthday))

# if age_string.startswith('eight'):
#     age_string = "n " + age_string
# else:
age_string = " " + age_string

soon_posts = []

f = open('data/blog/posts.json')
posts = json.load(f)
for post in posts:
    if not posts[post]['live']:
        soon_posts.append(int(posts[post]['id']))

soon_posts.sort()
soon_posts = soon_posts[0:1]
soon_posts[0] = str(soon_posts[0])

f = open('data/favorites/music/music_all_time.json')
all_time_music = json.load(f)
albums = len(all_time_music.keys())
total_score = 0
tens = 0
for album in all_time_music:
    total_score += all_time_music[album]['score']
    if all_time_music[album]['score'] == 10.0:
        tens += 1
avg_score = total_score/albums

app = Flask(__name__)
app.debug = True


app.config['SECRET_KEY'] = secret_key
Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('your favorite email: ', validators=[DataRequired()])
    submit = SubmitField('Submit')    


@app.route("/404")
def setup_404():
    return render_template("/error.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly

    return redirect("/404")
    # return render_template('error.html'), 404

# @app.route("/<page>")
# def main_page(page):
#     if os.path.exists(f'templates/{page}.html'):
#         return render_template(f'{page}.html')
#     else:
#         return render_template("error.html")

@app.route("/press")
def press():
    return render_template("about/news.html")
@app.route("/tools")
def tool():
    return render_template("tech.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")
# blogs

def get_emails():
    with open(f'./emails.json', 'r') as json_file:
        emails = json.load(json_file)
    return emails

@app.route("/qban2")
def qban2():
    return "01110101 01100111 01100111 01100011 01100110 00111010 00101111 00101111 01110001 01100101 01110110 01101001 01110010 00101110 01110100 01100010 01100010 01110100 01111001 01110010 00101110 01110000 01100010 01111010 00101111 01110001 01100101 01110110 01101001 01110010 00101111 01101000 00101111 00110000 00101111 01110011 01100010 01111001 01110001 01110010 01100101 01100110 00101111 00110001 01011111 01100110 01100110 01001100 01100110 01001010 01110100 01100011 01000110 00101101 01101000 01111010 01000110 01100101 01000111 00111000 01110101 01010010 01110011 01011001 01110101 01010000 01100001 01001101 00101101 01000110 01000111 00110011 01100101 01010110 01101011 01011010"


def store_emails(emails):
    with open('./emails.json', 'w') as json_file:
        json.dump(emails, json_file, indent=4)

def send_email(reciever, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASS)
    msg = f'Subject: {subject}\n\n{body}'
    return server.sendmail(EMAIL_ADDRESS, reciever, msg)
    
def confirm_email(email):
    #Step 1: Check email
    #Check using Regex that an email meets minimum requirements, throw an error if not
    addressToVerify = email
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        return "this email is in an invalid format!"

    emails = get_emails()
    if addressToVerify in list(emails.keys()):
        return "you have already signed up with this email!"

    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': addressToVerify})

    status = response.json()['status']
    if status == 'valid':
        return True
    else:
        return "this email does not exist!"

def add_email(email, emails):
    emails[email] = {
        'date': datetime.now(timezone('US/Eastern')).strftime("%d/%m/%Y %I:%M:%S")
    }
    store_emails(emails)


@app.route("/", methods=['GET', 'POST'])
def index(): 
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        email = form.name.data.lower()
        message = confirm_email(email.strip())
        if message == True:
            # send_email(email, 'Welcome to asboyer.com!', 'You are signed on for future updates regarding asboyer.com and Boyer\'s Blog!')
            form.name.data = ""
            add_email(email, get_emails())
            message = "thanks, you are signed up for updates!"

    return render_template("index.html", age=age_string, grade=grade, form=form, school=school, message=message)


@app.route("/blog", methods=['GET', 'POST'])
def blog():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        email = form.name.data.lower()
        message = confirm_email(email.strip())
        if message == True:
            # send_email(email, 'Welcome to asboyer.com!', 'You are signed on for future updates regarding asboyer.com and Boyer\'s Blog!')
            form.name.data = ""
            add_email(email, get_emails())
            message = "thanks, you are signed up for updates!"

    return render_template("blog/blog.html", form=form, message=message)

@app.route("/blog/<name>")
def blog_post(name):
    if name in soon_posts:
        title = "t"
        for post in posts:
            if posts[post]['id'] == int(name):
                title = posts[post]["title"]
                d = posts[post]["date"]
                subs = posts[post]["subjects"]
                blurb = posts[post]["blurb"]
                sub_str = ""
                for sub in subs:
                    if subs[len(subs) - 1] == sub:
                        sub_str += sub
                    else:    
                        sub_str += sub + ", "
                break
        return render_template("soon.html", value=title, date_string=d, subs=sub_str, blurb=blurb)
    elif os.path.exists(f'templates/blog/{name}.html'):
        return render_template(f"blog/{name}.html")
    else:
        # make error page
        return render_template("error.html")

# favorites


@app.route("/pics")
def gallery():
    return render_template("gallery.html")

@app.route("/data/gallery/pics.json")
def gallery_json():
    f = open('data/gallery/pics.json')
    data = json.load(f)
    return data


# music
@app.route("/music")
def music():
    return render_template("favorites/music/music.html", albums=albums, avg_score=round(avg_score, 2), tens=p.number_to_words(tens))

@app.route("/music/<name>")
def music_path(name):
    if os.path.exists(f'templates/favorites/music/{name}.html'):
        return render_template(f"favorites/music/{name}.html")
    else:
        # make error page
        return render_template("error.html")


# books
@app.route("/books")
def books():
    return render_template("favorites/books/books.html")

@app.route("/books/<name>")
def books_path(name):
    if os.path.exists(f'templates/favorites/books/{name}.html'):
        return render_template(f"favorites/books/{name}.html")
    else:
        # make error page
        return render_template("error.html")

@app.route("/data/books/shelf.json")
def bookshelf_json():
    f = open('data/favorites/books/shelf.json')
    data = json.load(f)
    return data


@app.route("/data/books/library.json")
def library_json():
    f = open('data/favorites/books/library.json')
    data = json.load(f)
    return data

@app.route("/data/books/list.json")
def booklist_json():
    f = open('data/favorites/books/list.json')
    data = json.load(f)
    return data

# movies
@app.route("/movies")
def movies():
    return render_template("favorites/movies/movies.html")


# movies
@app.route("/movies/to_watch")
def movies_to_watch():
    return render_template("favorites/movies/to_watch.html")

@app.route("/shows")
def shows():
    return render_template("favorites/shows/shows.html")

#SEO
@app.route("/robots.txt")
def se1():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def se2():
    return send_from_directory(app.root_path, "sitemap.xml")

@app.route("/data/movies.json")
def movies_json():
    f = open('data/favorites/films/movies.json')
    data = json.load(f)
    return data

@app.route("/data/to_watch.json")
def movies_json_to_watch():
    f = open('data/favorites/films/to_watch.json')
    data = json.load(f)
    return data

@app.route("/data/music_all_time.json")
def music_json():
    f = open('data/favorites/music/music_all_time.json')
    data = json.load(f)
    return data

@app.route("/data/music/to_listen.json")
def music_json_to_listen():
    f = open('data/favorites/music/music_to_listen.json')
    data = json.load(f)
    return data

@app.route("/data/music_current.json")
def music_json_current_albums():
    f = open('data/favorites/music/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/music_current_songs.json")
def music_json_current_tracks():
    f = open('data/favorites/music/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/data/shows.json")
def load_shows():
    f = open('data/favorites/films/shows.json')
    data = json.load(f)
    return data

@app.route("/data/projects.json")
def load_projects():
    f = open('data/projects/index.json')
    data = json.load(f)
    return data

@app.route("/data/news.json")
def load_news():
    f = open('data/about/press/news.json')
    data = json.load(f)
    return data

@app.route("/data/podcasts.json")
def load_pods():
    f = open('data/about/press/podcasts.json')
    data = json.load(f)
    return data

@app.route("/data/work.json")
def load_work():
    f = open('data/work/index.json')
    data = json.load(f)
    return data

@app.route("/data/skills.json")
def load_skills():
    f = open('data/about/services/services.json')
    data = json.load(f)
    return data

@app.route("/data/blog/posts.json")
def load_blog_posts():
    f = open('data/blog/posts.json')
    data = json.load(f)
    return data    

@app.route("/data/tools.json")
def load_tools():
    f = open('data/tools/index.json')
    data = json.load(f)
    return data  

@app.route("/data/midnight/specs.json")
def load_midnight_parts():
    f = open('data/midnight/parts.json')
    data = json.load(f)
    return data      

@app.route("/midnight")
def midnight_parts():
    return render_template("midnight/parts.html")

@app.route("/tools/midnight")
def midnight_parts_tools():
    return render_template("midnight/parts.html")

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/podcasts")
def pods():
    return render_template("about/podcasts.html")

@app.route("/highlights/bball_2022")
def bball_2022():
    return render_template("highlights/bball_2022.html")

@app.route("/data/highlights/bball_2022.json")
def load_bball_2022():
    f = open('data/highlights/bball_2022.json')
    data = json.load(f)
    return data  

@app.route("/data/quotes.json")
def load_quotes():
    f = open('data/quotes/quotes.json')
    data = json.load(f)
    return data
#####################3/1/2021 music backup here#####################
@app.route("/data/archive/music/312021/music_current.json")
def load_music_current_312021():
    f = open('data/archive/music/312021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/312021/music_current_songs.json")
def load_music_current_songs_312021():
    f = open('data/archive/music/312021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/0")
def music_archive_312021():
    return render_template("archive/music/312021.html")

#####################7/1/2021 music backup here#####################

@app.route("/data/archive/music/712021/music_current.json")
def load_music_current_712021():
    f = open('data/archive/music/712021/music_current.json')
    data = json.load(f)
    return data
        
@app.route("/data/archive/music/712021/music_current_songs.json")
def load_music_current_songs_712021():
    f = open('data/archive/music/712021/music_current_songs.json')
    data = json.load(f)
    return data
        
@app.route("/archive/music/1")
def music_archive_712021():
    return render_template("archive/music/712021.html")


#####################8/25/2021 music backup here#####################

@app.route("/data/archive/music/8252021/music_current.json")
def load_music_current_8252021():
    f = open('data/archive/music/8252021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/8252021/music_current_songs.json")
def load_music_current_songs_8252021():
    f = open('data/archive/music/8252021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/2")
def music_archive_8252021():
    return render_template("archive/music/8252021.html")
    
#####################9/10/2021 music backup here#####################

@app.route("/data/archive/music/9102021/music_current.json")
def load_music_current_9102021():
    f = open('data/archive/music/9102021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/9102021/music_current_songs.json")
def load_music_current_songs_9102021():
    f = open('data/archive/music/9102021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/3")
def music_archive_9102021():
    return render_template("archive/music/9102021.html")
    
#####################9/16/2021 music backup here#####################

@app.route("/data/archive/music/9162021/music_current.json")
def load_music_current_9162021():
    f = open('data/archive/music/9162021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/9162021/music_current_songs.json")
def load_music_current_songs_9162021():
    f = open('data/archive/music/9162021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/4")
def music_archive_9162021():
    return render_template("archive/music/9162021.html")
    
#####################10/3/2021 music backup here#####################

@app.route("/data/archive/music/1032021/music_current.json")
def load_music_current_1032021():
    f = open('data/archive/music/1032021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/1032021/music_current_songs.json")
def load_music_current_songs_1032021():
    f = open('data/archive/music/1032021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/5")
def music_archive_1032021():
    return render_template("archive/music/1032021.html")
    
#####################10/12/2021 music backup here#####################

@app.route("/data/archive/music/10122021/music_current.json")
def load_music_current_10122021():
    f = open('data/archive/music/10122021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/10122021/music_current_songs.json")
def load_music_current_songs_10122021():
    f = open('data/archive/music/10122021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/6")
def music_archive_10122021():
    return render_template("archive/music/10122021.html")
    
#####################10/27/2021 music backup here#####################

@app.route("/data/archive/music/10272021/music_current.json")
def load_music_current_10272021():
    f = open('data/archive/music/10272021/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/10272021/music_current_songs.json")
def load_music_current_songs_10272021():
    f = open('data/archive/music/10272021/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/7")
def music_archive_10272021():
    return render_template("archive/music/10272021.html")
    
#####################2/4/2022 music backup here#####################

@app.route("/data/archive/music/242022/music_current.json")
def load_music_current_242022():
    f = open('data/archive/music/242022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/242022/music_current_songs.json")
def load_music_current_songs_242022():
    f = open('data/archive/music/242022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/8")
def music_archive_242022():
    return render_template("archive/music/242022.html")
    
#####################3/27/2022 music backup here#####################

@app.route("/data/archive/music/3272022/music_current.json")
def load_music_current_3272022():
    f = open('data/archive/music/3272022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/3272022/music_current_songs.json")
def load_music_current_songs_3272022():
    f = open('data/archive/music/3272022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/9")
def music_archive_3272022():
    return render_template("archive/music/3272022.html")
    
#####################3/27/2022 music backup here#####################

#####################4/10/2022 music backup here#####################

@app.route("/data/archive/music/4102022/music_current.json")
def load_music_current_4102022():
    f = open('data/archive/music/4102022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/4102022/music_current_songs.json")
def load_music_current_songs_4102022():
    f = open('data/archive/music/4102022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/10")
def music_archive_4102022():
    return render_template("archive/music/4102022.html")
    
#####################5/8/2022 music backup here#####################

@app.route("/data/archive/music/582022/music_current.json")
def load_music_current_582022():
    f = open('data/archive/music/582022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/582022/music_current_songs.json")
def load_music_current_songs_582022():
    f = open('data/archive/music/582022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/11")
def music_archive_582022():
    return render_template("archive/music/582022.html")
    
#####################6/6/2022 music backup here#####################

@app.route("/data/archive/music/662022/music_current.json")
def load_music_current_662022():
    f = open('data/archive/music/662022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/662022/music_current_songs.json")
def load_music_current_songs_662022():
    f = open('data/archive/music/662022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/12")
def music_archive_662022():
    return render_template("archive/music/662022.html")
    
#####################6/23/2022 music backup here#####################

@app.route("/data/archive/music/6232022/music_current.json")
def load_music_current_6232022():
    f = open('data/archive/music/6232022/music_current.json')
    data = json.load(f)
    return data

@app.route("/data/archive/music/6232022/music_current_songs.json")
def load_music_current_songs_6232022():
    f = open('data/archive/music/6232022/music_current_songs.json')
    data = json.load(f)
    return data

@app.route("/archive/music/13")
def music_archive_6232022():
    return render_template("archive/music/6232022.html")
    