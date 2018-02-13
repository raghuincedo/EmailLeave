class MESSAGEFROMRMQ:
    def __init__(self):
        self.date_of_recieving_of_email = ''
        self.employee_who_send_email = ''
        self.email_body = ''
        self.email_subject = ''
        self.cc_list_in_email = ''

    def setrmqMessage(self, value):
        self.message_rmq = value

    def getrmqMessage(self):
        return self.message_rmq

    def setDateOfRecievingOfEmail(self, date):
        self.date_of_recieving_of_email = date
    def setEmployeeWhoSendEmail(self, mail_id):
        self.employee_who_send_email = mail_id
    def setEmailBody(self, text):
        self.email_body = text
    def setEmailSubject(self, subject):
        self.email_subject = subject
    def setCCListInEmail(self, cc_list):
        self.cc_list_in_email = cc_list


    def getDateOfRecievingOfEmail(self):
        return self.date_of_recieving_of_email
    def getEmployeeWhoSendEmail(self):
        return self.self.employee_who_send_email
    def getEmailBody(self):
        return self.email_body
    def getEmailSubject(self):
        return self.email_subject
    def getCCListInEmail(self):
        return self.cc_list_in_email
