from random import randint
from Input import ConsoleInput

class RockPaperScissors:

    userInput = ConsoleInput()

    def __init__(self):
        self.userInput = ConsoleInput()
        
    def determineWinner(self,player,computer):
        if player == computer:
            result = "Draw"
        elif (player + 1)%3 == computer:
            result = "Player wins"
        elif (computer + 1)%3 == player:
            result = "Computer Wins"
        return result

    def getUserChoice(self,weapons):
        for counter in range(len(weapons)):
            print("Select " + str(counter) + " for " + weapons[counter])
        player = self.userInput.getInputInt("Input one of the three options ")
        if player in [0,1,2]:
            print("You selected " + weapons[player])
        return player

    def getComputerChoice(self, weapons):
        chosen = randint(0, len(weapons)-1)
        print("Computer chose " + weapons[chosen])
        return chosen

    def getGame(self):
        starWars = ["Darth Vadar", "Emperor", "Luke Skywalker"]
        rockPaper = ["Paper", "Rock", "Scissors"]
        game = self.userInput.getInputString("Please select Star Wars or Rock,Paper Scissors")
        if game[0] == "S":
            weapon = starWars
        else:
            weapon = rockPaper
        return weapon

    def play(self):
        weapon = self.getGame()
        player = self.getUserChoice(weapon)
        while player in [0,1,2]:
            computer = self.getComputerChoice(weapon)
            result = self.determineWinner(player,computer)
            print(result)
            player = self.getUserChoice(weapon)

def main():
    RockPaperScissors.play()

rock = RockPaperScissors()
rock.play()
