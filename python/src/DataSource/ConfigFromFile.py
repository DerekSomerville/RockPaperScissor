from python.src.DataSource.Config import Config
from python.src.DataSource.RockConstants import RockConstants

class ConfigFromFile(Config):

    def getConfig(self):
        configPath = RockConstants.filePrefix + "Config/properties.cfg"
        propertyFile = open(configPath,"r")
        propertyData = propertyFile.read().splitlines()
        propertyFile.close()
        return propertyData
