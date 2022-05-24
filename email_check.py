import json, smtplib
from deepdiff import DeepDiff

from secret import EMAIL_ADDRESS, EMAIL_PASS, my_address
from email.mime.text import MIMEText

msg = MIMEText("""
You are signed on for future updates regarding asboyer.com and Boyer\'s Blog!
""")
msg['Subject'] = 'Welcome to asboyer.com!'
msg['To'] = EMAIL_ADDRESS

def get_new_emails():
    with open(f'/opt/asboyer/asboyer/emails.json', 'r') as json_file:
        new_emails = json.load(json_file)
    return new_emails

def get_old_emails():
    with open(f'/opt/asboyer/asboyer/email_backup.json', 'r') as json_file:
        old_emails = json.load(json_file)
    return old_emails

def send_email(recievers, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASS)
    return server.sendmail(EMAIL_ADDRESS, [EMAIL_ADDRESS] + recievers, msg)

def store_emails(emails):
    with open('/opt/asboyer/asboyer/email_backup.json', 'w') as json_file:
        json.dump(emails, json_file, indent=4)

def prep_emails():
    old_emails = get_old_emails()
    new_emails = get_new_emails()

    if old_emails == new_emails:
        pass
    else:
        diff = DeepDiff(old_emails, new_emails)
        emails = []
        for i in range(len(diff['dictionary_item_added'])):
            emails.append(diff['dictionary_item_added'][i][6:-2])
        send_email(emails, msg.as_string())
        store_emails(new_emails)
        print('new emails added and notified:')
        if len(emails) > 1:
            s = "s"
        else:
            s = ""
        email_string = f"New email{s} subscribed to asboyer.com:\n\n"
        for email in emails:
            print(email)
            email_string += email + "\n"
        new_msg = MIMEText(email_string)
        new_msg['Subject'] = f"New asboyer.com subscriber{s}"
        new_msg['To'] = my_address
        send_email([my_address], new_msg.as_string())
