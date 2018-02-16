

import smtplib
from email.message import EmailMessage


class EMAILSENDER:

    def __init__(self,host='mail.incedoinc.com',login='helpdesk_icf@incedoinc.com',
                 password='feb@2018'):
        self.host=host
        self.login=login
        self.password=password

    def sendMail(self,to="user_icf@incedoinc.com",subject="test_mail"
                 ,content="testing body",reply_to=None):

        Msg = EmailMessage()
        Msg.set_content(content)

        Msg['Subject'] = subject
        Msg['From'] = self.login
        Msg['To'] = to
        if reply_to:
            Msg.add_header("In-Reply-To",reply_to)
        Smtp_client = smtplib.SMTP(self.host)
        Smtp_client.login(self.login ,self.password)
        Smtp_client.send_message(Msg)
        Smtp_client.close()

send_email=EMAILSENDER()
reply_to='<24E10F677BCBF840AADB79B1C46F00F812811BA9@TS-GGN-MBX002.ibtechnology.com>'

send_email.sendMail(reply_to=reply_to)
