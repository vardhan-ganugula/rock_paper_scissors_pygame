"""   Created by Ganugula Vardhan  """
import random

#colors

def red():
    return ("\033[1;31m ")
def green():
    return ("\033[1;32m ")
def blue():
    return ("\033[1;34m ")
def white():
    return ("\033[1;37m ")
def banner():
    print(f""" \033[1;33m
          
#########################################
#        ____    ____    ____           #
#        |  _ \  |  _ \  / ___|         #
#        | |_) | | |_) | \___ \         #
#        |  _ <  |  __/   ___) |        #
#        |_| \_\ |_|     |____/         #
#        rock    paper   scissors       #
#                                       #
#########################################
{white()}
#    How to play ?
          
{blue()}choose 1 out of 3 options{green()}
          
    Rock     - > 1
    Paper    - > 2
    Scissors - > 3 {white()}
          
Rock beats scissors, Paper beats rock, Scissors beats paper

*************   Rules:  ************* {red()}
          
1. Only Numbers (1,2,3,0) are allowed 
2. 0 for exit          
{white()}
************************************* 

          """)
#game dictionary list

def game():

    #game banner and rules
    banner()


    gameList = {1:'rock', 2:'paper', 3:'scissors'}
    wins = 0
    loss = 0
    # always true for keep asking the input until it reaches to 0

    while(True):
        generatedChoice = (random.choice(list(gameList.keys())))
        try:
            choice = int(input("Enter the choice : rock (1) , paper (2) , scissors (3) > "))
        except ValueError:
            print(red() + '\nonly numbers are allowed \n restart the game \n Press any key to exit' + white() + '\n')
            break
        if choice>3 or choice <0:
            print(red() + '\nYou enterd wrong choice \n restart the game \n Press any key to exit' + white() + '\n')
            break
        elif choice == 0:
            print(f'\nGame Over. Your Score : {green()} {wins} {white()} | computer score : {red()} {loss} {red()} \n Press any key to exit' + '\n')
            break
        if choice != (generatedChoice):
            """  
            ### The main logic

            difference is 1 or -2 always to win

            if choice is 1 and generatedChoice is 3:
                print(f'you won : {choice} beats {generatedChoice} ')
            elif choice is 2 and generatedChoice is 1:
                print(f'you won : {choice} beats {generatedChoice} ')
            elif choice is 3 and generatedChoice is 2:
                print(f'you won : {choice} beats {generatedChoice} ')

            """
            if (choice - generatedChoice) == 1 or (choice - generatedChoice) == -2:
                wins+=1
                print(f'\nComputer choice : {gameList[generatedChoice]}\n\n {green()} you won : {gameList[choice]} beats {blue()}{gameList[generatedChoice]} {white()} \n')
            else:
                loss+=1
                print(f"\nComputer choice : {gameList[generatedChoice]}\n\n {red()} you loose : {gameList[choice]} won't beats {blue()}{gameList[generatedChoice]} {white()} \n")
        else:
            print(blue() + '\n Game tie ' + white() + '\n')

        print(f"Your Score :{green()} {wins} {white()} | Computer Score : {red()}{loss}{white()}\n\n")
if __name__ == '__main__':
    game()
    input()