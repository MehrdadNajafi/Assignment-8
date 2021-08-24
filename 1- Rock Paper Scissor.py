import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def win_or_lose():
    if scores['User'] == scores['Computer']:
        print(Fore.CYAN + 'the game is Tie. No one wins!!!')
    
    elif scores['User'] > scores['Computer']:
        print(Fore.CYAN + 'You Win !!!')

    elif scores['Computer'] > scores['User']:
        print(Fore.CYAN + 'Computer Win !!!')

def Check():
    if user_choice == computer_choice:
        print(Fore.CYAN + f"Both players selected {user_choice}. It's a tie!")
    
    elif user_choice == 'Rock':
        if computer_choice == 'Scissor':
            print(Fore.CYAN + 'Rock smashes scissors! You win!')
            scores['User'] += 1
        else:
            print(Fore.CYAN + 'Paper covers rock! You lose.')
            scores['Computer'] += 1
    
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print(Fore.CYAN + 'Paper covers rock! You win!')
            scores['User'] += 1
        else:
            print(Fore.CYAN + 'Scissors cuts paper! You lose.')
            scores['Computer'] += 1

    elif user_choice == 'Scissor':
        if computer_choice == 'Paper':
            print(Fore.CYAN + 'Scissors cuts paper! You win!')
            scores['User'] += 1
        else:
            print(Fore.CYAN + 'Rock smashes scissors! You lose.')
            scores['Computer'] += 1

def show_menu():
    print(F"Round {Round}, FIGHT!\n1- Rock\n2- Paper\n3- Scissor")

def show_scores():
    print(Fore.CYAN + f"User score: {scores['User']}\tComputer score: {scores['Computer']}")
    print('-' * 15)

Round = 0
options = ['Rock', 'Paper', 'Scissor']
scores = {'User' : 0, 'Computer' : 0}

for i in range(10):
    Round += 1
    show_menu()
    user_choice = int(input('Choose an option: '))
    user_choice = options[user_choice-1]
    computer_choice = random.choice(options)
    Check()
    show_scores()
win_or_lose()