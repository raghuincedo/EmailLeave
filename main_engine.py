from EmailCommunication import RabbitConfigurationLoader, RMQ_Email_receiver

class StartMainEngine:
    def __init__(self):
        ## initiate all neccessary classes and check connection
        self.rmq_email_reciever_obj = RMQ_Email_receiver.RMQEMAILRECIEVER()

    def processIncomingEmail(self):
        pass

    def processResponseOfIncomingEmail(self):
        pass

    def main(self):
        request_data = self.processIncomingEmail()
        response_data = self.processResponseOfIncomingEmail()
        print("Process Completed")

if __name__ == '__main__':
    rabbitConfigData = RabbitConfigurationLoader.rabbitConfigurationUploader().loadRmqConfigurationsFromJson()
    RMQ_Email_receiver.startEmailListenerProcess(rabbitConfigData)
    print("Email Reciever thread started")
