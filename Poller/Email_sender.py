

import smtplib
from email.message import EmailMessage


class EMAILSENDER:

    def __init__(self,host='mail.incedoinc.com',login='helpdesk_icf@incedoinc.com',
                 password='feb@2018'):
        self.host=host
        self.login=login
        self.password=password

    def sendMail(self,to="user_icf@incedoinc.com",subject="test_mail",content="testing body"):

        Msg = EmailMessage()
        Msg.set_content(content)

        Msg['Subject'] = subject
        Msg['From'] = self.login
        Msg['To'] = to

        Smtp_client = smtplib.SMTP(self.host)
        Smtp_client.login(self.login ,self.password)
        Smtp_client.send_message(Msg)
        Smtp_client.close()

send_email=EMAILSENDER()

send_email.sendMail()
