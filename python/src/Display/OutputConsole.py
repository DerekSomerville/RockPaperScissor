from python.src.Display.Output import Output
from python.src.DataSource.WriteToFile import WriteToFile

class OutputConsole(Output):

    writeToFile = True
    outputWriteToFile = WriteToFile("userOutputLog.csv")

    def print(self, output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)
