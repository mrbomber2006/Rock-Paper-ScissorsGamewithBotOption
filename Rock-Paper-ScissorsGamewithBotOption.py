import random
from colorama import Fore, Style
import os
the_choices = (1, 2, 3, 4)
computer_choices = (1, 2, 3)
player1_score = 0
player2_score = 0
player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name (or 'bot' to play with the computer): ")

print(Fore.YELLOW + "*** Type 4 to quit ***" + Style.RESET_ALL)
while True:
    try:

        choose1 = int(input(f"{player1}, please choose:\n1. Rock\n2. Paper\n3. Scissors\n(To quit, enter 4): "))
    
        os.system('cls' if os.name == 'nt' else 'clear')
        if choose1 == 4:
            break

        if player2 == "bot":
            choose2 = random.choice(computer_choices)
            print(Fore.YELLOW + "Bot is thinking..." + Style.RESET_ALL)

        else:
            print(Fore.YELLOW + "*" * 10 + Style.RESET_ALL)
            choose2 = int(input(f"{player2}, please choose:\n1. Rock\n2. Paper\n3. Scissors\n(To quit, enter 4): "))
        
        if (choose1 or choose2) not in the_choices:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        elif choose2 == 4:
            break
        elif choose1 == choose2:
            print(Fore.BLUE + "Tie!" + Style.RESET_ALL)
        elif choose1 == 1:
            if choose2 == 3:
                print(Fore.GREEN + f"{player1}, you won!" + Style.RESET_ALL)
                player1_score += 1
            elif choose2 == 2:
                print(Fore.GREEN + f"{player2}, you won!" + Style.RESET_ALL)
                player2_score += 1
        elif choose1 == 2:
            if choose2 == 1:
                print(Fore.GREEN + f"{player1}, you won!" + Style.RESET_ALL)
                player1_score += 1
            elif choose2 == 3:
                print(Fore.GREEN + f"{player2}, you won!" + Style.RESET_ALL)
                player2_score += 1
        elif choose1 == 3:
            if choose2 == 2:
                print(Fore.GREEN + f"{player1}, you won!" + Style.RESET_ALL)
                player1_score += 1
            elif choose2 == 1:
                print(Fore.GREEN + f"{player2}, you won!" + Style.RESET_ALL)
                player2_score += 1
        else:
            print(Fore.RED + "Something went wrong. Please try again." + Style.RESET_ALL)
        
        print(Fore.YELLOW + "*" * 10 + Style.RESET_ALL)
        if choose1 == 1:
            rps1 = "rock"
        elif choose1 == 2:
            rps1 = "paper"
        elif choose1 == 3:
            rps1 = "scissors"
        
        if choose2 == 1:
            rps2 = "rock"
        elif choose2 == 2:
            rps2 = "paper"
        elif choose2 == 3:
            rps2 = "scissors"
    
        print(f"{player1} chose {Fore.CYAN + rps1 + Style.RESET_ALL}!")
        print(f"{player1} score: {player1_score}")
        print(f"{player2} chose {Fore.CYAN + rps2 + Style.RESET_ALL}!")
        print(f"{player2} score: {player2_score}")
        print(Fore.YELLOW + "*" * 10 + Style.RESET_ALL)
    except BaseException:
        print(Fore.LIGHTRED_EX + "insert 1,2,3,or 4!".upper() + Style.RESET_ALL)
if player1_score > player2_score:
    print(f"{player1} is won the game!")
elif player1_score < player2_score:
    print(f"{player2} is won the game!")
else:
    print("Tie!")
print(Fore.LIGHTBLACK_EX + "done!")