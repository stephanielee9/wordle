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

def validate_guess():
    pass

def format_guess(guess):
    '''
    formats input
    '''

    word = ''
    for letter in guess:
        word += f'{letter.upper()} '
    return(word)






def main():

    with open('common_words.txt', 'r') as f:
        words = f.read().upper().split()
        words_list = [x for x in words if len(x) == 5]

    guesses = []
    print_guesses(guesses)
    word = random.choice(words_list)

    for _ in range(6):
        guess = input(color.RED + color.BOLD + '>>> ' + color.END)
        while not (guess.isalpha() and len(guess) == 5):
            guess = input(color.RED + color.BOLD + '>>> ' + color.END)
        guesses.append(format_guess(guess))
        print_guesses(guesses)





    # print(word)


if __name__== "__main__":
    main()