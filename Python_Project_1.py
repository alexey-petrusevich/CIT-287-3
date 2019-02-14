# CIT-287
# Project 3
# Date submitted: April 7, 2018
# Professor: Arland J. Richmond
# Student: Aliaksei Petrusevich

import random
import sys
import os

# SETUP INITIAL VALUES
###############################################################

firstWin = (7, 11)
firstLose = (2, 3, 12)
secondLose = 7
fileName = "scores.txt"
bet = 100
baseScore = 1000
score = baseScore
winnings = 0

# LOAD SCORES
###############################################################
scores = []

if os.path.exists(fileName) == True:
    infile = open(fileName, "r")

    s = infile.readline()
    while len(s) != 0:
        record = {} # make empty dictionary
        strings = s.split("#") # split strings "name" and "score"
        record["name"] = strings[0] # add "name" entry into disctionary
        record["score"] = int(strings[1]) # add "score" entry into disctionary
        scores.append(record) # append disctionary to the list of records
        s = infile.readline() # read next line

    infile.close()

# ENTER NAME
###############################################################

name = input("Enter your name: ")

found = False

for i in scores:
    if i["name"] == name:
        score = i["score"]
        found = True
        break
    
if found == True:
    print("\nWelcome back, " + name + "! Your last score was " + str(score) + "!")
else:
    print("\nWelcome, " + name + "!")
        
# DISPLAY MENU
###############################################################

choice = ""

while choice != "5":
    print("\n*********************")
    print("Craps")
    print("*********************\n")
    print("1. Play the game")
    print("2. Display Available Funds")
    print("3. Reset Winnings to Zero")
    print("4. Save Name and Score")
    print("5. Quit")

    print("-----------------------------")
    choice = input("Enter your choice: ")


# PLAY GAME
###############################################################
    if choice == "1":
        # play game
        print("\n-----------------------------")
        if score < bet:
            print("\nNot enough funds to play!\n")
            
        else:
            while True:
                roll = input("\nType 'R' key to roll the dice: ")
                if roll.lower() != 'r':
                    print("\nYou must type 'R' or 'r' key to roll the dice!")
                    print("\nPress 'Enter' key to continue...")
                    input()
                    continue
                break
            
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            diceSum = die1 + die2

            print("\n-----------------------------")
            print("You first roll is " + str(diceSum))
            print("-----------------------------")
            
            if diceSum in firstWin:
                print("\nYou won " + str(bet) + " points!")
                print("-----------------------------")
                score += bet
                winnings += bet
            elif diceSum in firstLose:
                print("\nYou lost " + str(bet) + " points!")
                print("-----------------------------")
                score -= bet
                winnings -= bet
            else:

                point = diceSum
                print("Your 'point' is " + str(point))
                print("-----------------------------")
                
                while True:
                    roll = input("\nType 'R' key to roll the dice: ")
                    if roll.lower() != 'r':
                        print("\nYou must type 'R' or 'r' key to roll the dice!")
                        print("\nPress 'Enter' key to continue...")
                        input()
                        continue

                    
                    die1 = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    diceSum = die1 + die2
                    print("\n-----------------------------")
                    print("Your next roll is " + str(diceSum))
                    print("-----------------------------")
                    
                    if diceSum == point:
                        print("You won " + str(bet) + " poins!")
                        print("-----------------------------")
                        score += bet
                        winnings += bet
                        
                    elif diceSum == secondLose:
                        print("You lost " + str(bet) + " points!")
                        print("-----------------------------")
                        score -= bet
                        winnings -= bet
                        
                    else:
                        print("\nRoll again...")
                        continue
                    
                    break
                
            if (score <= 0):
                print("-----------------------------")
                print("\nGAME OVER - You are out of funds!")
                print("-----------------------------")
                input("\nPress 'Enter' key to continue...")
                sys.exit()
            else:
                input("\nPress 'Enter' key to continue...")

# DISPLAY AVAILABLE FUNDS
###############################################################

    elif choice == "2":
        # display available funds
        print("\n-----------------------------")        
        print("Starting balance: " + str(score - winnings))
        print("Winnings:", str(winnings) if winnings > 0  else "0")
        print("Available funds: " + str(score))
        print("-----------------------------")
        input("\nPress 'Enter' key to continue...")

# RESET WINNINGS
###############################################################        
    elif choice == "3":
        print("-----------------------------")
        # reset winnings
        if winnings > 0:
            
            print("\nResetting winnings : " + str(winnings))
            choice = input("\nAre you sure? (Y/N): ")
            
            while choice.lower() != 'y' and choice.lower() != 'n':
                print("\nYou must enter 'Y' or 'N' keys only!")
                print("\nResetting winnings (" + str(winnings) + ")")
                choice = input("\nAre you sure? (Y/N): ")
                
            if choice.lower() == 'y':
                score -= winnings
                winnings = 0
                print("\n-----------------------------")
                print("Winnings have been reset to 0!")
                print("-----------------------------")
            
        else:
            print("\nThere are no winnings to reset!")

# SAVE
###############################################################

    elif choice == "4":
        # save name and score
        outfile = open(fileName, 'w')

        if len(scores) == 0:
            outfile.write(name + '#' + str(score) + '\n')
        else:

            for i in scores:
                if i["name"] == name:
                    continue
                else:
                    outfile.write(i["name"] + '#' + str(i["score"]) + '\n')

            # rewrite data
            outfile.write(name + '#' + str(score) + '\n')
            
        outfile.close()
        print("\n-----------------------------")
        print("Data saved...")
        print("-----------------------------")

# QUIT
###############################################################
        
    elif choice == "5":
        # quit
        print("\nQuitting the game...")
        choice = input("\nAre you sure? (Y/N): ")
            
        while choice.lower() != 'y' and choice.lower() != 'n':
            print("\nYou must enter 'Y' or 'N' keys only!")
            print("\nQuitting the game...")
            choice = input("\nAre you sure? (Y/N): ")

        if choice.lower() == 'y':
            break;
        
    else:
        # invalid choice
        print("-----------------------------")
        print("\nError! You must select options 1 to 5 only!")
        print("-----------------------------")

###############################################################

print("\nThank you for playing!")
    
