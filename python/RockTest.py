import Rock, unittest

class rockTests(unittest.TestCase):

    def test_determinWinnerRockRock(self):
        result = Rock.determineWinner(0,0)
        self.assertEqual("Draw", result)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()