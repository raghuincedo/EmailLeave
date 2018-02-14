from DbStorage.DB_connection_maker import client
from ConfigFilesLoader import db_config_data

db_name = db_config_data['database_info']['name']

def get_from_collection(collection_name = "",
                         json_data = {}):
    """
    - > checks if json data is a dict object, else return None
    - > returns json data if found
    :param collection_name: name of the collection in which data is to be inserted
    :param json_data: dict object
    :return: json data if found
    """
    if type(json_data) is not dict:
        print("json data is not a dict object")
        return None

    return client[db_name][collection_name].find_one(json_data)


