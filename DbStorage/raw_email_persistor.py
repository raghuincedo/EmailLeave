from DbStorage.DB_connection_maker import client
from ConfigFilesLoader import db_config_data
from ConfigurationFiles.DB_collection_templates import raw_emails_template

db_name = db_config_data['database_info']['name']
collection_name = db_config_data['database_info']['collections']['rawEmails']

class RawEmailsPersistor(object):
    """
    - > help
    """
    def __init__(self):
        """
        - > insert template data in to collection
        """
        if client[db_name][collection_name].count() == 0:
            self.InsertIntoRawEmails(json_data = raw_emails_template)

    def InsertIntoRawEmails(self, json_data = {}):
        """
        - > inserts json data in user collection
        :param json_data: dict data
        :return: true if succesful else false
        """
        if type(json_data) is not dict:
            print("json data is not a dict object")
            return False

        client[db_name][collection_name].insert_one(json_data)
        print("Record inserted in {} succesfully".format(collection_name))
        return True

    def FetchFromRawEmails(self, json_key = {}):
        """
        - > fetch record from database containing json_key
        :param json_key: dict object
        :return: matched record
        """
        if type(json_key) is not dict:
            print("json data is not a dict object")
            return None

        return client[db_name][collection_name].find_one(json_key)

    def CheckRequestIdExists(self, request_id = ""):
        """
        - > checks if input json containing request id exists in the collection
        :param request_id: string containing requestId
        :return: True if request id exists else false
        """
        if self.FetchFromRawEmails(json_key = {"requestID": request_id}) is not None:
            return True
        else:
            return False