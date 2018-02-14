from DbStorage.DB_connection_maker import client
from ConfigFilesLoader import db_config_data

db_name = db_config_data['database_info']['name']

def insert_in_collection(collection_name = "",
                         json_data = {}):
    """
    - > checks if json data is a dict object, returns false if not
    - > appends the json data in collection with name as collection_name
    :param collection_name: name of the collection in which data is to be inserted
    :param json_data: dict object
    :return: true if inserted in database else false
    """
    if type(json_data) is not dict:
        print("json data is not a dict object")
        return False

    client[db_name][collection_name].insert_one(json_data)
    return True

