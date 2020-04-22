class SingletonWriteToFile:
    # Here will be the instance stored.
    __instance = None
    file = ""
    filePath = "C:/Users/Derek/Documents/GitHub/RockPaperScissor/resource/log/inputLog.csv"

    @staticmethod
    def getInstance():
        """ Static access method. """
        if SingletonWriteToFile.__instance == None:
            SingletonWriteToFile()
        return SingletonWriteToFile.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SingletonWriteToFile.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SingletonWriteToFile.__instance = self

    def writeToFile(self,user,logItem):
        if self.file == "":
            self.file = open(filePath,"a")
        self.file.write(user + "," + logItem)
