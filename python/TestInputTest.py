from InputTest import InputTest
from WriteToFile import WriteToFile
from Rock import RockPaperScissors
from InputConsole import InputConsole
from unittest.mock import MagicMock
from ReadFileToList import ReadFileToList

#rock = RockPaperScissors()
#rock.play()

#userInput = InputTest()
#userInput.inputList = [1,2,5]
#print(userInput.getInputInt(""))
#print(userInput.getInputInt(""))

#inputConsole = InputConsole()
#inputConsole.getInputString = MagicMock(side_effect=[1,2,5])
#print(inputConsole.getInputInt(""))

#fileToList = ReadFileToList()
#print(fileToList.getList("userInputLog.csv"))

fileToList = ReadFileToList()
print(fileToList.getList("userInputLog.csv"))
inputConsole = InputConsole()
inputConsole.getInputString = MagicMock(side_effect=fileToList.getList("userInputLog.csv"))
print(inputConsole.getInputInt(""))
print(inputConsole.getInputInt(""))
print(inputConsole.getInputInt(""))

#fileToList = ReadFileToList()
#inputConsole = InputConsole()
#inputConsole.getInputString = MagicMock(side_effect=fileToList.getList("userInputLog.csv"))
#print(inputConsole.getInputString(""))
