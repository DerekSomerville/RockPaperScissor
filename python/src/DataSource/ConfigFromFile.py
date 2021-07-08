from python.src.DataSource.Config import Config
from python.src.DataSource.RockConstants import RockConstants
import os

class ConfigFromFile(Config):

    def fixWorkingDirectory(self):
        currentWorkingDirectory = os.getcwd()
        while "test" in currentWorkingDirectory or "src" in currentWorkingDirectory:
            os.chdir("../")
            currentWorkingDirectory = os.getcwd()

    def getConfig(self):
        self.fixWorkingDirectory()
        configPath = RockConstants.filePrefix + "Config/properties.cfg"
        propertyFile = open(configPath,"r")
        propertyData = propertyFile.read().splitlines()
        propertyFile.close()
        return propertyData
