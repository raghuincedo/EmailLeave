import json, os, logging
from paths import PROJECT_ROOT


logger = logging.getLogger(__name__)

class rabbitConfigurationUploader:

    def loadRmqConfigurationsFromJson(self):
        rabbitConFigDict = {}
            ## build path to rabbitConfigFile
        rabbitConfigFile = PROJECT_ROOT
        rabbitConfigFile = os.path.join(rabbitConfigFile, 'ConfigurationFiles')
        rabbitConfigFile = os.path.join(rabbitConfigFile, 'RmqConfigFile.json')

        try:
            with open(rabbitConfigFile, 'r') as rabbitConFigFP:
                rabbitConFigDict = json.load(rabbitConFigFP)
            rabbitConFigFP.close()

        except FileNotFoundError:
            message= 'rabbitConFigFile not found at '+ rabbitConfigFile
            logger.error(message)
            exit(37)

        return rabbitConFigDict