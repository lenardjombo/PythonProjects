import random

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed:
        print(f"\nWord: {guessed}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            guessed = "".join([letter if letter == guess or letter in guessed_letters else "_" for letter in word])
        else:
            attempts -= 1
            print("Wrong guess!")
    
    if "_" not in guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nSorry, you lost. The word was: {word}")

hangman()
