import Rock, unittest,ConfigFromStubb

class rockTests(unittest.TestCase):

    def test_determinWinnerRockRock(self):
        rock = Rock.RockPaperScissors()
        result = rock.determineWinner(0,0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequest(self):
        rock = Rock.RockPaperScissors()
        rock.setConfig(ConfigFromStubb.ConfigFromStubb())
        result = rock.generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
