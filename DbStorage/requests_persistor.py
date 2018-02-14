from DbStorage.DB_connection_maker import client
from ConfigFilesLoader import db_config_data
from ConfigurationFiles.DB_collection_templates import requests_template

db_name = db_config_data['database_info']['name']
collection_name = db_config_data['database_info']['collections']['requests']

class RequestsPersistor(object):
    """
    - > help
    """
    def __init__(self):
        """
        - >
        """
        self.InsertIntoRequests(json_data = requests_template)

    def InsertIntoRequests(self, json_data = {}):
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

    def FetchFromRequests(self, json_key = {}):
        """
        - > fetch record from database containing json_key
        :param json_key: dict object
        :return: matched record
        """
        if type(json_key) is not dict:
            print("json data is not a dict object")
            return None

        return client[db_name][collection_name].find_one(json_key)
