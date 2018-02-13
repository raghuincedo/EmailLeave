class MESSAGEFROMRMQ:
    def __init__(self):
        self.date_of_recieving_of_email = ''
        self.requester_email = ''
        self.email_body = ''
        self.email_subject = ''
        self.cc_list_in_email = ''
        self.requester_name = ''

    def setrmqMessage(self, value):
        self.message_rmq = value

    def getrmqMessage(self):
        return self.message_rmq

    def setDateOfRecievingOfEmail(self, date):
        self.date_of_recieving_of_email = date
    def setEmailBody(self, text):
        self.email_body = text
    def setEmailSubject(self, subject):
        self.email_subject = subject
    def setCCListInEmail(self, cc_list):
        self.cc_list_in_email = cc_list
    def setRequesterName(self, email):
        try:
            self.requester_name = email.strip('>').split("<")[0]
        except:
            self.requester_name = None
    def setRequesterEmail(self, email):
        try:
            self.requester_email = email.strip('>').split("<")[1]
        except:
            self.requester_email = None

    def getRequesterEmail(self):
        return self.requester_email
    def getRequesterName(self):
        return self.requester_name
    def getDateOfRecievingOfEmail(self):
        return self.date_of_recieving_of_email
    def getEmailBody(self):
        return self.email_body
    def getEmailSubject(self):
        return self.email_subject
    def getCCListInEmail(self):
        return self.cc_list_in_email
