from random import randint
from InputConsole import InputConsole
from OutputConsole import OutputConsole
from ConfigFromFile import ConfigFromFile

class RockPaperScissors:

    userInput = InputConsole()
    userOutput = OutputConsole()
    config = ConfigFromFile()
    property = []

    def __init__(self):
        self.userInput = InputConsole()

    def setUserInput(self,userInput):
        self.userInput = userInput

    def setUserOutput (self,userOutput):
        self.userOutput = userOutput

    def setConfig(self,config):
        self.config = config

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
            self.userOutput.print("Select " + str(counter) + " for " + weapons[counter])
        player = self.userInput.getInputInt("Input one of the three options ")
        if player in [0,1,2]:
            self.userOutput.print("You selected " + weapons[player])
        return player

    def getComputerChoice(self, weapons):
        chosen = randint(0, len(weapons)-1)
        self.userOutput.print("Computer chose " + weapons[chosen])
        return chosen

    def getListOfGames(self):
        if self.property == []:
            self.property = self.config.getConfig()
        listOfGames = []
        for counter in range(1,len(self.property)):
            listOfGames.append(self.property[counter].split(":")[0])
        return listOfGames

    def getWeaponLists(self):
        if self.property == []:
            self.property = self.config.getConfig()
        weaponLists = []
        for counter in range(1,len(self.property)):
            weaponLists.append(self.property[counter].split(":")[1].split(","))
        return weaponLists

    def getGamesRequest(self,listOfGames):
        request = "Please select"
        for counter in range(len(listOfGames)):
            request += " " + str(counter) + " - " + listOfGames[counter]
        return request

    def generateGamesListRequest(self):
        listOfGames = self.getListOfGames()
        request = self.getGamesRequest(listOfGames)
        return request

    def getGame(self):
        starWars = ["Darth Vadar", "Emperor", "Luke Skywalker"]
        rockPaper = ["Paper", "Rock", "Scissors"]
        request = self.generateGamesListRequest()
        userGame = self.userInput.getInputInt(request)
        weaponsLists = self.getWeaponLists()
        return weaponsLists[userGame]

    def play(self):
        weapon = self.getGame()
        player = self.getUserChoice(weapon)
        while player in [0,1,2]:
            computer = self.getComputerChoice(weapon)
            result = self.determineWinner(player,computer)
            self.userOutput.print(result)
            player = self.getUserChoice(weapon)

def main():
    rock = RockPaperScissors()
    rock.play()



