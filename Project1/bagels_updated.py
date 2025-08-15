"""
Project 1 - Bagels Game
Big book of small python projects

Practice using constants

Updating Project with Red/Green/Yellow rules
Clue locations are fixed, not sorted
"""

import random
NUM_DIGITS = 4
MAX_GUESSES = 10

def main():
    print('''Numeric Deductive logic game.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. You have {} guesses.'''.format(NUM_DIGITS, MAX_GUESSES))
    print('''Here are some clues:
    When I say:     That means:
    Red             The number is not correct in any position
    Green           The number is in the correct position
    Yellow          The number is in the wrong position
    
    
    For example, if the secret number is 248 and your guess is 843,
    the clues would be Red Green Yellow.''')

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.' .format(secretNum))

        print('Do you want to play again? (Yes or No)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    numbers = list('0123456789') #List of digits 0-9
    random.shuffle(numbers) #shuffles the list into a random order

    #get the first NUM_Digits digits in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the clues"""

    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Green')
        elif guess[i] in secretNum:
            clues.append('Yellow')
        else:
            clues.append('Red')
    return ' '.join(clues)
    
if __name__=='__main__':
    main()