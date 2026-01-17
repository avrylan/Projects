import random

x = random.randint(1, 100)
found = False
guesses = 5

while found != True and guesses != 0:
    y = int(input("Enter a number between 1 and 100: "))
    print()
    if y < x:
        print ("Number is greater than", y)
        guesses -= 1
        print ("Number of guesses remaining = ", guesses)
        print()
    elif y > x :
        print ("Number is smaller than", y)
        guesses -= 1
        print ("Number of guesses remaining = ", guesses)
        print()
    else :
        print ("Congratulations, Answer is", y)
        found = True