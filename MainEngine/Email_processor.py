from MainEngine.Email_validator import EMAILVALIDITY
from MainEngine.request_ID_exists import *
from MainEngine.request_ID_not_exists import *

class PROCESSINCOMINGEMAIL:
    def __init__(self):
        self.email_validity_checker = EMAILVALIDITY()
    def processMessage(self, original_email):
        ## get email_id
        email_id = original_email
        subject = original_email
        valid = self.email_validity_checker.CheckSourceOfEmail(email_id)
        if valid:
            request_id_exist = self.email_validity_checker.CheckforRequestIdExistance(subject)
            if request_id_exist:
                # check extra validity and send message to user with existing requestID in subject line
                # update database
                # self.processResponseMessage(validity_mode)
                pass
            else:
                #process request_id_not_exist
                #self.processResponseMessage(validity_mode)
                pass # don't send any message check for extra content, cancel, valid email etc.
    def processResponseMessage(self, validity_mode):
        # call Email_responder
        pass