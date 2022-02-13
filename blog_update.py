import json, smtplib, requests
from secret import EMAIL_ADDRESS, EMAIL_PASS
from email.mime.text import MIMEText

def get_new_post():
    with open(f'/opt/asboyer/asboyer/blog.json', 'r') as json_file:
        posts = json.load(json_file)
    url = "https://asboyer.com/data/blog/posts.json"
    r = requests.get(url)
    current_posts = r.json()
    current_post_titles = []
    for title in current_posts:
        if current_posts[title]['live'] == True:
            current_post_titles.append(title)
    if posts['live_posts'] != current_post_titles:
        r =  list(set(current_post_titles) - set(posts['live_posts']))
        posts['live_posts'] = current_post_titles
        with open(f'/opt/asboyer/asboyer/blog.json.json', 'w') as json_file: 
            json.dump(posts, json_file, indent=4)
        data = {}
        data['title'] = r[0]
        data['date'] = current_posts[r[0]]['date']
        data['subjects'] = current_posts[r[0]]['subjects']
        data['id'] = current_posts[r[0]]['id']
        data['img'] = current_posts[r[0]]['cover_img']
        return data
    return {}

def send_email(recievers, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASS)
    return server.sendmail(EMAIL_ADDRESS, [EMAIL_ADDRESS] + recievers, msg)


def get_emails():
    with open(f'/opt/asboyer/asboyer/emails.json', 'r') as json_file:
        new_emails = json.load(json_file)
    return list(new_emails.keys())

def new_blog_post():
    data = get_new_post()
    if data != {}:
        subject_str = ""
        for i in range(len(data['subjects'])):
            if i == len(data['subjects']) - 1:
                subject_str += data['subjects'][i]
            else:
                subject_str += data['subjects'][i] + ', '

        status = f"""new asboyer.com blogpost!
asboyer.com/blog/{str(data['id'])}
title: {data['title']}
date: {data['date']}
subjects: {subject_str}
"""        
        msg = MIMEText(status)
        msg['Subject'] = data['title']
        msg['To'] = EMAIL_ADDRESS
        send_email(get_emails(), msg.as_string())
        print('emails sent for new blog post')


if __name__ == '__main__':
    new_blog_post()
