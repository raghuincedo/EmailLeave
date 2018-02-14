from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import ConnectionFailure
from ConfigFilesLoader import db_config_data, logger_name
import Logger
import logging

logger = logging.getLogger(logger_name)
db_name = db_config_data['database_info']['name']
collection_names = db_config_data['database_info']['collections']

client = MongoClient(host = db_config_data['host'], port = db_config_data['port'])
db = client.admin

## Logic needs to be written in case some connection failure happens

if db_config_data['database_info']['name'] not in client.database_names():
    database = client[db_config_data['database_info']['name']]
    logger.info("Database created succesfully")
else:
    logger.info("Database already exists")

