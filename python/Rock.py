from random import randint


class RockPaperScissors:

    def __init__():
        this.userInput = ConsoleInput()
        
    def determineWinner(player,computer):
        if player == computer:
            result = "Draw"
        elif (player + 1)%3 == computer:
            result = "Player wins"
        elif (computer + 1)%3 == player:
            result = "Computer Wins"
        return result

    def getUserChoice(weapons):
        for counter in range(len(weapons)):
            print("Select " + str(counter) + " for " + weapons[counter])
        player = this.userInput.getInputInt("Input one of the three options ")
        if player in [0,1,2]:
            print("You selected " + weapons[player])
        return player

    def getComputerChoice(weapons):
        chosen = randint(0, len(weapons)-1)
        print("Computer chose " + weapons[chosen])
        return chosen

    def getGame():
        starWars = ["Darth Vadar", "Emperor", "Luke Skywalker"]
        rockPaper = ["Paper", "Rock", "Scissors"]
        game = this.userInput.getInputString("Please select Star Wars or Rock,Paper Scissors")
        if game[0] == "S":
            weapon = starWars
        else:
            weapon = rockPaper

        return weapon

    def play():
        weapon = getGame()
        player = getUserChoice(weapon)
        while player in [0,1,2]:
            computer = getComputerChoice(weapon)
            result = determineWinner(player,computer)
            print(result)
            player = getUserChoice(weapon)

RockPaperScissors.play()
