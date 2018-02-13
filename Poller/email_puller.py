# -*- coding: utf-8 -*-

import imaplib
import email
import pickle

# new mail generator --> yield after each mail to save resources
def new_mail(last_uid, host, port, login, password):
    # connect
    mail_server = imaplib.IMAP4(host, port)

    # authenticate
    mail_server.login(login, password)
    mail_server.select('inbox')

    # issue the search command of the form "SEARCH UID 42:*"
    command = "UID {}:*".format(last_uid)
    result, data = mail_server.uid('search', None, command)
    messages = data[0].split()
    #print(messages)
    # yield mails
    for message_uid in messages:
        # SEARCH command *always* returns at least the most
        # recent message, even if it has already been synced
        if int(message_uid) > last_uid:
            result, data = mail_server.uid('fetch', message_uid, '(RFC822)')
            print('Message %s\n%s\n' % (int(message_uid), data[0][1]))
            # yield raw mail body

            yield data[0][1]


# usage example
for mail in new_mail(last_uid=2,
                               host='mail.incedoinc.com', port=143,
                               login='helpdesk_icf@incedoinc.com',
                               password='feb@2018'):


    with open('saved_email.pkl', 'wb') as output:
        pickle.dump(mail, output, pickle.HIGHEST_PROTOCOL)

    email_message = email.message_from_bytes(mail)
    print(email_message)
    #print(email_message[From])
    if email_message.is_multipart():
        for part in email_message.get_payload():
            print(part.get_payload())
    else:
        a=1
        print(email_message.get_payload(decode=True))

    # do something useful with raw mail
    pass
