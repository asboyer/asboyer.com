from blog_update import send_email, get_emails
from email.mime.text import MIMEText
from secret import EMAIL_ADDRESS

with open('./update_message.txt', 'r') as f:
    lines = f.readlines()
f = open('./update_message.txt', 'w+')
f.close()

text = ""
for i in range(len(lines)):
    if i != 0:
        text += lines[i].strip() + '\n'

msg = MIMEText(text)
msg['Subject'] = lines[0].strip()
msg['To'] = EMAIL_ADDRESS
ems = get_emails()
ems.remove(EMAIL_ADDRESS)
send_email(ems, msg.as_string())
print('update sent!')