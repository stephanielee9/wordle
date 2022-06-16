'''
simple python version of wordle
'''

import random
random.seed(3)

def print_guesses(guess_list):

    '''
    prints guessed words and remaining guesses
    '''

    blanks = 6 - len(guess_list)
    for guess in guess_list:
            print(guess)
    for _ in range(blanks):
        print('_ _ _ _ _')

def print_letters(letter_list):
    '''
    prints unused letters for remaining guesses
    '''

    




def main():

    with open('common_words.txt', 'r') as f:
        words = f.read().upper().split()
        words_list = [x for x in words if len(x) == 5]

    guesses = ['test', 'test']
    word = random.choice(words_list)

    print_guesses(guesses)





    print(word)


if __name__== "__main__":
    main()