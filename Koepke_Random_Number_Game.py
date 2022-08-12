#**********************************************************
# File: Koepke_Random_Number_Game.py
# Programmer: Robert Koepke
# Class: CEIS110 Summer2022
# Instructor: Prof. Ng
#*********************************************************
# This program is a guess the number game. The program
# generates a random number and asks the user to guess
# the number. The user has 10 guesses to guess the number
# correctly. After the user guesses, the program will tell 
# the user if they're guess is too high or too low. The
# game ends once the user wins or runs out of tries. The user
# then has the option to play again. This game is also a 
# lot of fun (I promise)!
#*********************************************************

import random #for random number generator
import os #for clear screen
from time import sleep # for delays to help avoid errors
                       # during clear screen

#********************************************************
# getGuess
#********************************************************
# This function takes no arguments and gets a valid guess
# from the user that is an integer and is between 0 and
# 100. The function then returns the guess to the caller.
#********************************************************

def getGuess():
    # initiates guess to -1 so as not to confuse the while
    # loop
    guess = -1
    
    # loops until the user enters a guess between 0 and 100
    while (guess < 0) or (guess > 100):
        while True:
            # loops until the user enters a number
            try:
                guess = int(input('Enter a guess between 0 and 100: '))
                break
            except ValueError:
                print('\nNumbers only silly!! Try again...\n')
                sleep(1)
        
        # displays if the user enters a number outside the
        # valid range
        if (guess < 0) or (guess > 100):
            print('\nNumbers between 0 and 100 please!\n')
            sleep(1)
    
    return guess

#********************************************************
# main
#********************************************************    

def main():
    # clear screen to begin game
    os.system('cls')
    sleep(2)
    print('\nWelcome to the random number guessing game!')
    
    # default values
    response = 'y'
    guesses = []
    tries = 10
    win = False
    
    # This while loop allows the user to play the game more than
    # once if desired
    while response.lower() == 'y':
        # generate random number
        randNum = random.randint(1, 100)
        print('\nGood Luck! You have {} tries to guess the number!\n'.format(tries))
        
        # call to getGuess to get user guess
        guesses.append(getGuess())
        #update number of tries
        tries -= 1
        
        # correct guess first try
        if guesses[len(guesses)-1] == randNum:
            print('\nYou Guessed it!! and in one try!! Are you a God? (The answer is yes)')
            sleep(2)
            win = True
        # incorrect guess first try
        elif guesses[len(guesses) - 1] > randNum:
            print('\nLol. Your guess was too high.')
            sleep(2)
        else:
             print('\nLol. Your guess was too low.')
             sleep(2)
             
        # the rest of the 9 tries are done in this while loop. I set it up this way
        # so that the next responses are different than the first guess to give the
        # game more variety. This loop will continue until tries reach 0 or the
        # user wins the game.
        while tries > 0 and win is False:
            # clears screen for each new try
            os.system('cls')
            sleep(1)
            
            # New message if there's only one try left
            if tries == 1:
                print('\nOne try left... Dont mess this up dummy!')
                sleep(2)
            # this else block generates a random response of three responses
            # that only appear if the user gets the number wrong
            else:
                rPrompt = random.randint(1, 3)
                
                if rPrompt == 1:
                    print('\nReally?... That number?...')
                    sleep(1)
                elif rPrompt == 2:
                    print('\nTry again dummy...')
                    sleep(1)
                else:
                    print('\nIve seen cats do better and cats cant type...')
                    sleep(2)
            
            # clears screen for new get guess prompt
            os.system('cls')
            sleep(2)
                
            # reminds user of their most recent guess so they know to guess higher or lower
            if guesses[len(guesses)-1] > randNum:
                print('\nYour last guess of {} was too high.\n'.format(guesses[len(guesses)-1]))
            else:
                print('\nYour last guess of {} was too low.\n'.format(guesses[len(guesses)-1]))
                
            # displays number of tries
            if tries == 1:
                print('You have 1 try left. Pressure is on!\n')
            else:
                print('You have {} tries left.\n'.format(tries))
            
            # gets another user guess
            guesses.append(getGuess())
            #update tries
            tries -= 1
            
            # dispays when user gets the number correct in two or more tries
            if guesses[len(guesses)-1] == randNum:
                print('\nHey! You Guessed it!!')
                sleep(2)
                win = True
            # wrong guess. restart loop.
            elif guesses[len(guesses)-1] > randNum:
                print('\nYour guess was too high you silly goose!')
                sleep(2)
            else:
                print('\nYour guess was too low little miss Guess-is-too-low!') 
                sleep(2)
        
        # clears screen after the user wins or loses to display results
        os.system('cls')
        sleep(2)
        
        # user has won the game message
        if win is True:
            if tries == 9:
                print('\nCongratulations!!!\nYou guessed it in 1 try!!')
            else:
                print('\nCongratulations!!!\nYou guessed it in {} tries!!'.format(10 - tries))
        # user has lost the game message
        else:
            print('\nYOU LOSE!! Here are your results:')
        
        # dispalys the number they were attempting to guess as well as their
        # previous guesses
        print('\nRandom number: {}\nYour guesses: {}'.format(randNum, guesses))
        response = input('\nTry a new number? (y/n): ')
        os.system('cls')
        sleep(2)
          
        # ensures responses are correct                                       
        while response.lower() != 'n' and response.lower() != 'y':
            print('\nIncorrect response!')
            response = input('\nTry again? (y/n): ')
            os.system('cls')
            sleep(2)
        
        # restarts the game
        if response.lower() == 'y':
            print('\nAlright! Lets go again!!! Gernating new random number...')
            # reseting variables to default values
            guesses[:] = []
            tries = 10
            win = False
            sleep(2)
            os.system('cls')
            sleep(2)
        # ends of game message
        else:
            #Goodbye message                                            
            print('\nThanks for playing!')
            sleep(2)

if __name__ == '__main__':
    main()
    
#End of Program