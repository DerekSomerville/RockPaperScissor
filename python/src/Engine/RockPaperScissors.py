from random import randint
from python.src.Display.InputConsole import InputConsole
from python.src.Display.OutputConsole import OutputConsole
from python.src.DataSource.ConfigFromFile import ConfigFromFile
from python.src.DataSource.ConfigFromStub import ConfigFromStub
from python.src.Display.InputRandom import InputRandom

class RockPaperScissors:

    userInput = InputConsole()
    userOutput = OutputConsole()
    computerInput = InputRandom()
    config = None
    property = None

    def __init__(self,config=ConfigFromFile()):
        self.config = config
        self.property = config.getConfig()

    def setUserInput(self,userInput):
        self.userInput = userInput

    def setComputerInput(self,computerInput):
        self.computerInput = computerInput

    def setUserOutput (self,userOutput):
        self.userOutput = userOutput

    def setConfig(self,config):
        self.config = config
        self.property = config.getConfig()

    def determineWinner(self,player,computer):
        if player == computer:
            result = "Draw"
        elif (player + 1)%3 == computer:
            result = "Player wins"
        elif (computer + 1)%3 == player:
            result = "Computer Wins"
        return result

    def getUserChoiceRequest(self,weapons):
        request = "Select "
        for counter in range(len(weapons)):
            request += str(counter) + " for " + weapons[counter] + " "
        return request

    def getUserChoice(self,weapons):
        request = self.getUserChoiceRequest(weapons)
        player = self.userInput.getInputInt(request)
        if player in [0,1,2]:
            self.userOutput.print("You selected " + weapons[player])
        return player

    def getComputerChoice(self, weapons):
        chosen = self.computerInput.getInputInt("")
        self.userOutput.print("Computer chose " + weapons[chosen])
        return chosen

    def setProperty(self):
        if self.property == []:
            self.property = self.config.getConfig()

    def getListOfGames(self):
        self.setProperty()
        listOfGames = []
        for counter in range(1,len(self.property)):
            listOfGames.append(self.property[counter].split(":")[0])
        return listOfGames

    def getWeaponLists(self):
        self.setProperty()
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

if __name__ == "__main__":
    main()




