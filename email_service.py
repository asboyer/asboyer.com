import email_check, blog_update
import time

while True:
    blog_update.new_blog_post()
    email_check.prep_emails()
    time.sleep(2)