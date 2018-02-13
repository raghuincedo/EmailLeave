from DbStorage.getter_setter import MESSAGEFROMRMQ
from MainEngine.Email_processor import PROCESSINCOMINGEMAIL
import email
import pickle

class EMAILRECIEVER:
    def __init__(self, recieved_message):
        self.message_rmq = MESSAGEFROMRMQ()
        self.message_rmq.setrmqMessage(recieved_message)

    def EmailMessageHandler(self, data):
        with open('../Poller/saved_email.pkl', 'rb') as input:
            email_message = pickle.load(input)
        message_processor = PROCESSINCOMINGEMAIL()
        #data = self.message_rmq.getrmqMessage()
        #data = data.decode('utf8')
        email_message = email.message_from_bytes(email_message)
        self.message_rmq.setDateOfRecievingOfEmail(email_message['date'])
        self.message_rmq.setCCListInEmail(email_message['cc'])
        self.message_rmq.setEmailBody(email_message.get_payload())
        self.message_rmq.setEmailSubject(email_message['subject'])
        self.message_rmq.setRequesterName(email_message['from'])
        self.message_rmq.setRequesterEmail(email_message['from'])
        message_processor.processMessage(self.message_rmq)

email_rec = EMAILRECIEVER('asdasd')
email_rec.EmailMessageHandler('abc')