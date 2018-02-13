class EMAILVALIDITY:
    def __init__(self):
        pass
    def CheckSourceOfEmail(self,email_id):
        domain = email_id.split('@')[1]
        if domain.lower() == 'incedoinc.com':
            return True
        else:
            return False

    def CheckforRequestIdExistance(self, subject_of_email):
        ##extract request ID from subject
        ##check requestID in database
        ##return True/False
        pass
    def contentValidator(self):
        ##
        pass