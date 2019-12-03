from random import randint

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
    player = int(input("Input one of the three options "))
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
    game = input("Please select Star Wars or Rock,Paper Scissors")
    if game[0] == "S":
        weapon = starWars
    else:
        weapon = rockPaper

    return weapon

def main():
    weapon = getGame()
    player = getUserChoice(weapon)
    while player in [0,1,2]:
        computer = getComputerChoice(weapon)
        result = determineWinner(player,computer)
        print(result)
        player = getUserChoice(weapon)

#main()