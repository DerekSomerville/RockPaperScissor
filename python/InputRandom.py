from Input import Input
from random import randint
from WriteToFile import WriteToFile

class InputRandom(Input):

    writeToFile = True
    inputWriteToFile = WriteToFile("computerInputLog.csv")

    def getInputString(self, request):
        return getInputInt

    def getInputInt(self, request):
        rand = randint(0, 2)
        if self.writeToFile:
            self.inputWriteToFile.writeToFile(rand)
        return rand
