import Rock, unittest,ConfigFromStub,ConfigFromFile
from unittest.mock import MagicMock
from InputTest import InputTest
from OutputTest import OutputTest
from ReadFileToList import ReadFileToList

class rockTests(unittest.TestCase):

    rock = Rock.RockPaperScissors()

    def test_determinWinnerRockRock(self):
        result = self.rock.determineWinner(0,0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        self.rock.setConfig(ConfigFromStub.ConfigFromStub())
        result = self.rock.generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_GenerateGamesRequestMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star Wars:Darth Vadar,Emperor,Luke Skywalker")
        self.rock.config.getConfig = MagicMock(return_value=propertyData)
        result = self.rock.generateGamesListRequest();
        print(result)
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_GenerateGamesRequestMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star Wars:Darth Vadar,Emperor,Luke Skywalker")
        config = ConfigFromFile.ConfigFromFile()
        config.getConfig = MagicMock(return_value=propertyData)
        self.rock.setConfig(config)
        result = self.rock.generateGamesListRequest();
        print(result)
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def getUserInput(self,inputs):
        userInput = InputTest()
        userInput.inputList = inputs
        return userInput

    def getComputerInputs(self,inputs):
        computerInput = InputTest()
        computerInput.inputList = inputs
        return computerInput

    def testRockVersusRock(self):
        self.rock.setConfig(ConfigFromStub.ConfigFromStub())
        self.rock.userInput = self.getUserInput([0,0,4])
        self.rock.computerInput = self.getComputerInputs([0])
        userOutput = OutputTest()
        self.rock.userOutput = userOutput
        self.rock.play()
        result = userOutput.outputlist.pop(-1)
        self.assertEqual(result,"Draw")

    def testReplay(self):
        self.rock.setConfig(ConfigFromStub.ConfigFromStub())
        fileToList = ReadFileToList()
        self.rock.userInput = self.getUserInput(fileToList.getList("userInputLog.csv"))
        self.rock.computerInput = self.getComputerInputs(fileToList.getList("computerInputLog.csv"))
        fileOutput = fileToList.getList("userOutputLog.csv")
        userOutput = OutputTest()
        self.rock.userOutput = userOutput
        self.rock.play()
        print(userOutput.outputlist)
        print(fileOutput)
        self.assertEqual(userOutput.outputlist,fileOutput)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
