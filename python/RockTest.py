import Rock, unittest,ConfigFromStub,ConfigFromFile
from unittest.mock import MagicMock

class rockTests(unittest.TestCase):

    def test_determinWinnerRockRock(self):
        rock = Rock.RockPaperScissors()
        result = rock.determineWinner(0,0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        rock = Rock.RockPaperScissors()
        rock.setConfig(ConfigFromStub.ConfigFromStub())
        result = rock.generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_GenerateGamesRequestMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star Wars:Darth Vadar,Emperor,Luke Skywalker")
        rock = Rock.RockPaperScissors()
        rock.config.getConfig = MagicMock(return_value=propertyData)
        result = rock.generateGamesListRequest();
        print(result)
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_GenerateGamesRequestMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star Wars:Darth Vadar,Emperor,Luke Skywalker")
        config = ConfigFromFile.ConfigFromFile()
        rock = Rock.RockPaperScissors()
        config.getConfig = MagicMock(return_value=propertyData)
        rock.setConfig(config)
        result = rock.generateGamesListRequest();
        print(result)
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
