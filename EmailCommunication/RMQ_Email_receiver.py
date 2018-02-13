import pika, logging, time, threading
from EmailCommunication import Email_reciever

def make_connection(obj, method, num):
    obj.credentials = pika.PlainCredentials(obj.rabbitConfigData["userName"],
                                            obj.rabbitConfigData["password"])
    obj.parameters = pika.ConnectionParameters(obj.rabbitConfigData["host"],
                                               int(obj.rabbitConfigData["port"]),
                                               '/', obj.credentials, heartbeat_interval=0)
    queues = obj.rabbitConfigData["queues"]
    keys = obj.rabbitConfigData["keys"]
    obj.connection = pika.BlockingConnection(obj.parameters)
    obj.channel = obj.connection.channel()
    obj.channel.queue_declare(queue=queues[num], durable=True)
    obj.channel.queue_bind(exchange=obj.rabbitConfigData["exchange"],
                           queue=queues[num],
                           routing_key=keys[num])
    obj.channel.basic_qos(prefetch_count=0)
    obj.channel.basic_consume(method, queues[num],
                              no_ack=True)
    obj.channel.start_consuming()


class RMQEMAILRECIEVER(threading.Thread):
    def __init__(self, rabbitConfigData):
        threading.Thread.__init__(self)
        self.rabbitConfigData = rabbitConfigData

    def run(self):
        try:
            make_connection(self, self.handleEmailMessagePersistence, 0)
        except:
            print("Thread cannot be started")

    def handleEmailMessagePersistence(self,receivedMessage):
        print(receivedMessage)
        email_msg_obj = Email_reciever.EMAILRECIEVER(receivedMessage)
        email_msg_obj.EmailMessageHandler()


def startEmailListenerProcess(rabbitConfigData):
    RMQEMAILRECIEVER(rabbitConfigData).start()