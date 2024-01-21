import random
#===================================== data =======================================================/
gameList = {
    "Number Guessing Game":{
        "description": "A game where it chooses a number and you guess it.",
        "price": 200,
        "stars": 4,
        "cashBack": 100
    },
    "Rock Paper Scissor Shoot":{
        "description": "A dangerous game, I mean you know it",
        "price": 100,
        "stars": 2,
        "cashBack": 50
    },
    "Thieves Game":{
        "description": "The mother of games that will keep you awake for weeks",
        "price": 600,
        "stars": 3,
        "cashBack": 300
    }
}
userGames = []
accountPoints = 250
# ====================================== functions ==================================================/
# --------------------------------------- Lambdas --------------------------------------------/

title = lambda x : print ("//" * len(x) + "\n" + " " * int(len(x)/2) + x + "\n" + "//" * len(x))
spacer = lambda x : print(x * 10)
balanceInfo = lambda x: print ("==" * int(len(x)/3) , x , "==" * int(len(x)/3))

# ------------------------------------- store Menu -----------------------------------------------/
def store():
    print("\n"*3)
    global userName
    global accountPoints
    while True:
        title("  The store of thieves  ")
        
        balanceInfo(f"{userName.title()} your have {accountPoints}$")
        print()
        num = 1
        for gameName, gameVal in  gameList.items():
            print(f"[ {num} ]: {gameName} => {gameVal.get('price')}$")
            num += 1
        print ("[ Q ]: Quit")
    
        showGame = input("Enter:")
        if showGame.lower() == "q":
            break
        elif int(showGame) <= len(gameList) and int(showGame) > 0:
            
            gameTitle = list(gameList)[int(showGame)-1]
            gameInfo = (gameList.get(gameTitle))
            title(gameTitle)
            print (f"Description: {gameInfo.get('description')}")
            print (f"Price: {gameInfo.get('price')}")
            print (f"Stars: {gameInfo.get('stars')}/5")
            print (f"Win Cash Back: {gameInfo.get('cashBack')}$")
            while True:
                spacer("==")
                buyAns = input("Whould you like to buy it? Y/N: ")
                
                if buyAns.lower() == "y":
                    if gameTitle in userGames:
                        spacer("==")
                        print ("you already Have it dumpy")
                    elif gameInfo.get("price") > accountPoints:
                        spacer("==")
                        print("you're poor now, you cannot afford it")
                    else:
                        userGames.append(gameTitle)
                        accountPoints -= gameInfo.get("price")
                        spacer("==")
                        print(f"we stole {gameInfo.get('price')} from your wallet.")
                        print("it's in your Game list now.")
                        print(f'you have {accountPoints} in your wallet')
                        
                elif buyAns.lower() == "n":
                    break
                else:
                    print("invalid input!")
        else:
            print("we Don't have this game yet")
# --------------------------------------- Games -------------------------------------------------/
# --------------- Number Guess Game --------------------/
def numGuesGame():
    print("\n"*3)
    global accountPoints
    title("Welcome To Number Guessing Game")
    while True:
        print ("[ Q ]: Quit")          
        topRange = str(input("Choose a number bigger than 5: "))
        if topRange.lower() == "q":
            break
        elif topRange.isalpha():
            print ("Only Numbers")
        elif int(topRange) <= 5:
            print("I said bigger than 5!! :|")
        else:
            randNum = random.randint(0, int(topRange))
            for i in range(int(int(topRange)/3), 0 , -1):
                spacer("==")
                print(f"you have {i} times of trying")
                ans = int(input("take a guess: "))
                if ans < randNum:
                    print("Go Bigger")
                elif ans > randNum:
                    print("Go lesser")
                elif ans == randNum:
                    accountPoints += 50
                    title("SUCESS!!, We Added 50$ To Your Wallet")
                    break
                elif i == 1:
                    print("you Loose :( ")
                else:
                    pass
            playAgain = input("Would you like to play again? Y/N: ")
            if playAgain.lower() == "y":
                pass
            else:
                break
# --------------- Rock Paper Scissor Game --------------------/  
def rPSGame():
    global accountPoints

    options = ["rock", "paper", "scissors"]
    title("Welcome To Rock Paper Scissor Game")
    while True:
        userWins = 0
        computerWins = 0


        while True:
            print(f"SCORE:\nYou:{userWins}\nme:{computerWins}")
            randNum = random.randint(0, 2)
            for j in options:
                print (f"[ {options.index(j)} ]: {j} ")
            try:
                spacer("====")
                
                if computerWins == 2:
                    accountPoints -= 25
                    print("you Lost :D; we took 25$ of your balance\nSorry if no one tells you that :(;")
                    break
                elif userWins == 2:
                    accountPoints += 50
                    print("shit!! You Won; Ok, we added 50$ in your balance")
                    break
                ans = int(input("Shoot: ").lower())
                spacer("====")
                if ans == 0 and randNum == 0:
                    print (f"No Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 1 and randNum == 1:
                    print (f"No Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 2 and randNum == 2:
                    print (f"No Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 0 and randNum == 1:
                    computerWins +=1
                    print (f"You Loos!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 0 and randNum == 2:
                    userWins +=1
                    print (f"You Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 1 and randNum == 0:
                    userWins +=1
                    print (f"You Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 1 and randNum == 2:
                    computerWins +=1
                    print (f"You Loos!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 2 and randNum == 0:
                    computerWins +=1
                    print (f"You Loos!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                elif ans == 2 and randNum == 1:   
                    userWins +=1
                    print (f"You Win!,\nyou chose {options[ans]} and I chose {options[randNum]}")
                else:
                    print("Invalid Input!!")
            except ValueError:
                print("invalid input")
        playAgain = input("Would you like to play again? Y/N: ")
        if playAgain.lower() == "y":
            pass
        else:
            break
# --------------- Thieves Game --------------------/
def thievesGame():
    return ("The Game has not been invented yet!\nsorry for your lost :,( ")

# ------------------------------------- Start Games ---------------------------------------------/
def startGame(theGame):
    if theGame.lower() == "number guessing game":
        numGuesGame()
    elif theGame.lower() == "rock paper scissor shoot":
        rPSGame()
    elif theGame.lower() == "thieves game":
        thievesGame()
    else:
        return
        
# ------------------------------------- Games Menu ----------------------------------------------/
def gamesMenu():
    print("\n"*3)
    while True:
        title("  My Boring Games  ")
        if len(userGames) == 0:
            print("you Have no Games!, Go to store and get one")
            print ("[ Q ]: Quit")
            ans = input("Enter: ")
            if ans.lower() == "q":
                break
            else:
                print("invalid input")
        else:
            print("Choose a game you want to play")
            for game in userGames:
                print(f"[ {userGames.index(game) + 1 } ]: {game}")
            print ("[ Q ]: Quit")
            ans = input("what game you choose? :")
            if ans.lower() == "q":
                    break
            elif int(ans) > len(userGames) and int(ans) < 0:
                print("Do you see a game we don't!!!")
            else:
                gameChoice = userGames[int(ans)-1]
                startGame(gameChoice)
        

# ------------------------------------- Main Menu -----------------------------------------------/
def main():
    
    while True:
        print("\n"*3)
        try:
            title("Boring Consol Main Menu")
            balanceInfo(f"{userName.title()} you have {accountPoints}$")
            print()
            print ("[ 1 ]: My Games\n[ 2 ]: Store" )
            choice = int(input("Enter:"))
            if choice == 1:
                gamesMenu()
            elif choice == 2:
                store()
            else:
                print("wrong input!")
        except ValueError:
            print("wrong input!")
# ====================================== App Start =======================================================/        
print ("##" * 29)
title("Welcome To The Boring Console")
print ("##" * 29)
userName = input("Your Name: ")
main()