import time
import random

#ensures that the player can roll dice however many times they like
loop = True
while loop == True:
    #generates random value between 1 and 6
    print("You rolled", random.randint(1, 6))
    answer = input("Roll again? Y/N")#allows user to go again if they wish
    if answer == "Y":
        continue
    elif answer == "N":
        loop == False
        quit()


    
