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
   BLACK = '\x1b[30m'
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

def print_letters(letters_green, letters_yellow, letters_grey):
    '''
    prints unused letters for remaining guesses
    '''

    letters = list('abcdefghijklmnopqrstuvwxyz'.upper())
    print('')
    for i in range(26):
        if letters[i] in letters_green:
            print(color.GREEN + color.BOLD + letters[i] + color.END + ' ', end='')
        elif letters[i] in letters_yellow:
            print(color.YELLOW + color.BOLD + letters[i] + color.END + ' ', end='')
        elif letters[i] in letters_grey:
            print(color.GREY + color.BOLD + letters[i] + color.END + ' ', end='')
        else:
            print(color.BLACK + color.BOLD + letters[i] + color.END + ' ', end='')
        if i % 9 == 0 and i != 0:
            print('')
    print('')

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


def format_guess(guess, word, letters_green, letters_yellow, letters_grey):
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
            letters_green.append(guess[i].upper())
        elif guess[i].upper() in word:
            formatted_guess += color.YELLOW + color.BOLD + guess[i].upper() + color.END + " "
            letters_yellow.append(guess[i].upper())
        else:
            formatted_guess += color.GREY + color.BOLD + guess[i].upper() + color.END + " "
            letters_grey.append(guess[i].upper())
    return formatted_guess, letters_green, letters_yellow, letters_grey

def main():

    with open('scrabble_5.txt', 'r') as f:
        words = f.read().upper().split()
        words_list = [x for x in words if len(x) == 5]

    setting = input('Random word? (y/n) >>> ')
    while setting not in ['y', 'n']:
        setting = input('Random word? (y/n) >>> ')
    
    if setting == 'y':
        word = random.choice(words_list)
    else:
         with open('word.txt', 'r') as f:
            word = f.read().upper()
    
    guesses = []
    letters_green = [] # correctly guessed letters
    letters_yellow = [] # almost correctly guessed letters
    letters_grey = []  # incorrectly guessed letters
    print_guesses(guesses)
    print_letters(letters_green, letters_yellow, letters_grey)


    for _ in range(6):
        guess = input(color.PURPLE + color.BOLD + '>>> ' + color.END)
        # while not (guess.isalpha() and len(guess) == 5):
        while not validate_guess(guess, words_list):
            guess = input(color.PURPLE + color.BOLD + '>>> ' + color.END)
        formatted_guess, letters_green, letters_yellow, letters_grey = format_guess(guess, word, letters_green, letters_yellow, letters_grey)
        guesses.append(formatted_guess)
        print_guesses(guesses)
        print_letters(letters_green, letters_yellow, letters_grey)
        if guess.upper() == word:
            print(color.PURPLE + color.BOLD + '\nYOU WIN! \n' + color.END)
            break
        if guess.upper() != word and _ == 5:
            print(color.RED + color.BOLD + '\nLEWSERRR \n' + color.END)


if __name__== "__main__":
    main()