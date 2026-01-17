import random

user = input("Rock, Paper, Scissors or Exit to Quit: ")

while user != "Exit" :
    num = random.randint(1,3)
    if num == 1:
        print("Computer played: Rock")
        if user == "Rock" :
            print("TIE")
        if user == "Scissors" :
            print("WON")
        if user == "Paper":
            print("LOSE")

    if num == 2:
        print("Computer played: Paper")
        if user == "Rock" :
            print("LOSE")
        if user == "Scissors" :
            print("WON")
        if user == "Paper":
            print("TIE")

    if num == 3:
        print("Computer played: Scissors")
        if user == "Rock" :
            print("WON")
        if user == "Scissors" :
            print("TIE")
        if user == "Paper":
            print("LOSE")
    
    user = input("Rock, Paper, Scissors or Exit to Quit: ")

