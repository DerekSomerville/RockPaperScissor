from InputTest import InputTest
from WriteToFile import WriteToFile

userInput = InputTest()
userInput.inputList = [1,2,5]
print(userInput.getInputInt(""))

writeToFile = WriteToFile()
print(writeToFile.filePath)
writeToFile.writeToFile("User","0")
