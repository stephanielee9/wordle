'''
simple python version of wordle
'''

import random
random.seed(3)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   GREY = '\x1b[37m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_guesses(guess_list):

    '''
    prints guessed words and remaining guesses
    '''

    print('')
    blanks = 6 - len(guess_list)
    for guess in guess_list:
            print(guess)
    for _ in range(blanks):
        print('_ _ _ _ _')

def print_letters(letter_list):
    '''
    prints unused letters for remaining guesses
    '''

    pass

def validate_guess(guess, words_list):
    
    checks = 0
    if guess.isalpha():
        checks += 1
    if len(guess) == 5:
        checks += 1
    if guess.upper() in words_list:
        checks += 1
    
    if checks == 3:
        return True
    else:
        return False


def format_guess(guess, word):
    '''
    formats input
    adds spaces between letters and capitalizes letters

    if letter is in correct position, green
    if letter is in word but not correct position, yellow
    else, grey
    '''

    formatted_guess = ''
    for i in range(5):
        if guess[i].upper() == word[i]:
            formatted_guess += color.GREEN + color.BOLD + guess[i].upper() + color.END + " "
        elif guess[i].upper() in word:
            formatted_guess += color.YELLOW + color.BOLD + guess[i].upper() + color.END + " "
        else:
            formatted_guess += color.GREY + color.BOLD + guess[i].upper() + color.END + " "
    return(formatted_guess)

def main():

    with open('scrabble_5.txt', 'r') as f:
        words = f.read().upper().split()
        words_list = [x for x in words if len(x) == 5]

    word = random.choice(words_list)
    print(word)
    guesses = []
    print_guesses(guesses)

    for _ in range(6):
        guess = input(color.PURPLE + color.BOLD + '>>> ' + color.END)
        # while not (guess.isalpha() and len(guess) == 5):
        while not validate_guess(guess, words_list):
            guess = input(color.PURPLE + color.BOLD + '>>> ' + color.END)
        guesses.append(format_guess(guess, word))
        print_guesses(guesses)





if __name__== "__main__":
    main()