from python.src.DataSource.Config import Config

class ConfigFromFile(Config):

    def getConfig(self):
        configPath = "../../../resource/Config/properties.cfg"
        propertyFile = open(configPath,"r")
        propertyData = propertyFile.read().splitlines()
        propertyFile.close()
        return propertyData
