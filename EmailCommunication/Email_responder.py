import smtplib
from email.message import EmailMessage
from ConfigFilesLoader import email_config_data

class EMAILRESPONDER:

    def __init__(self,
                 host = email_config_data['host'],
                 login = email_config_data['login_id'],
                 password = email_config_data['password']):
        self.host=host
        self.login=login
        self.password=password

    def sendMail(self,to="user_icf@incedoinc.com", subject="test_mail", content="testing body"):

        msg = EmailMessage()
        msg.set_content(content)

        msg['Subject'] = subject
        msg['From'] = self.login
        msg['To'] = to

        Smtp_client = smtplib.SMTP(self.host)
        Smtp_client.login(self.login ,self.password)
        Smtp_client.send_message(msg)
        Smtp_client.close()

send_email=EMAILRESPONDER()

send_email.sendMail()
