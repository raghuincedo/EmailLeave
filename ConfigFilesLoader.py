from paths import path_to_configuration_files
import os
import json

def return_DB_config_file():
    try:
        with open(os.path.join(path_to_configuration_files, "DbConfigFile.json")) as json_data:
            data = json.load(json_data)
            json_data.close()
        return data
    except FileNotFoundError:
        print("DBConfigFile.json does not exists at" + os.path.join(path_to_configuration_files, "DbConfigFile.json"))

def return_AD_config_file():
    try:
        with open(os.path.join(path_to_configuration_files, "ADConfigFile.json")) as json_data:
            data = json.load(json_data)
            json_data.close()
        return data
    except FileNotFoundError:
        print("ADConfigFile.json does not exists at" + os.path.join(path_to_configuration_files, "ADConfigFile.json"))

def return_Email_config_file():
    try:
        with open(os.path.join(path_to_configuration_files, "EMailConfigFile.json")) as json_data:
            data = json.load(json_data)
            json_data.close()
        return data
    except FileNotFoundError:
        print("EMailConfigFile.json does not exists at" + os.path.join(path_to_configuration_files, "EMailConfigFile.json"))

def return_Rmq_config_file():
    try:
        with open(os.path.join(path_to_configuration_files, "RmqConfigFile.json")) as json_data:
            data = json.load(json_data)
            json_data.close()
        return data
    except FileNotFoundError:
        print("RmqConfigFile.json does not exists at" + os.path.join(path_to_configuration_files, "RmqConfigFile.json"))

db_config_data = return_DB_config_file()
ad_config_data = return_AD_config_file()
email_config_data = return_Email_config_file()
rmq_config_data = return_Rmq_config_file()
logger_name = "MainLogger"