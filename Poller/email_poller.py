# -*- coding: utf-8 -*-

import imaplib
import email
import time
from ConfigFilesLoader import email_config_data

# new mail generator --> yield after each mail to save resources
class EMAILPOLLER():
    def __init__(self,
                 last_uid = None,
                 host = email_config_data['host'],
                 port = email_config_data['port'],
                 login = email_config_data['login_id'],
                 password = email_config_data['password']):

        self.last_uid=last_uid
        self.host=host
        self.port=port
        self.password=password
        self.login=login
        self.sleep_time=2

    def newMail(self):
        mail_server = imaplib.IMAP4(self.host, self.port)

        mail_server.login(self.login, self.password)
        mail_server.select('inbox')

        if self.last_uid is None:
            command='UNSEEN'
        else:
            command = "UID {}:*".format(self.last_uid)
        result, data = mail_server.uid('search', None, command)
        messages = data[0].split()

        for message_uid in messages:
            if self.last_uid is None or int(message_uid)>self.last_uid:
                result, data = mail_server.uid('fetch', message_uid, '(RFC822)')
                self.last_uid=int(message_uid)
                # yield raw mail body

                yield data[0][1]
        mail_server.close()
        mail_server.logout()

    def pollerLoop(self):

        while(1):
            flag_1=0
            for mail in email_poller.newMail():
                email_message = email.message_from_bytes(mail)
                print(email_message)
            flag_1+=1

            time.sleep(self.sleep_time)
            if flag_1==0 and self.sleep_time<3:
                self.sleep_time*=2
            print(self.sleep_time)


email_poller=EMAILPOLLER()
email_poller.pollerLoop()

'''
if email_message.is_multipart():
    for part in email_message.get_payload():
        print(part.get_payload())
else:
    a=1
    print(email_message.get_payload(decode=True))

'''
