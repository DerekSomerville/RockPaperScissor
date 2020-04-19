from Config import Config

class ConfigFromFile(Config):

    def getConfig(self):
        configPath = "C:/Users/Derek/Documents/GitHub/RockPaperScissor/java/Config/properties.cfg"
        propertyFile = open(configPath,"r")
        return propertyFile.readlines()

