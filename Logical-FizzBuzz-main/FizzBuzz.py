import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'''A logic game 
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
    Meaning
1. Fizz     - One digit is correct but in the wrong position.
2. Buzz     - One digit is correct and in the right position.
3. FizzBuzz - No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be: Buzz Fizz.''')

    while True:  # main game loop
        secret_num = get_secret_num()
        print('I have thought up a number!')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}:')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                print('You guessed it!')
                break  # They are correct so break out of the loop

            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses!')
                print(f'The answer was {secret_num}.')

        # Ask the player if they want to play again
        print('Do you want to play again? (Yes or No)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')

def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)  # shuffle them into random order
    secret_num = ''.join(numbers[:NUM_DIGITS])
    return secret_num

def get_clues(guess, secret_num):
    """Returns a string with the Fizz, Buzz, FizzBuzz clues for a guess and secret number."""
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Buzz')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Fizz')
    
    if len(clues) == 0:
        return 'FizzBuzz'  # There are no correct digits at all.
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
