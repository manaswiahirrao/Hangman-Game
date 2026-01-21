# Task 1: Hangman Game

import random
words = ["apple", "banana", "orange", "grapes", "mango"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 6
display_word = ["_"] * len(secret_word)

print("Welcome to Hangman Game")
print("Guess the word:", " ".join(display_word))

while wrong_guesses > 0 and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Letter already guessed")
    elif guess in secret_word:
        guessed_letters.append(guess)
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct guess")
    else:
        guessed_letters.append(guess)
        wrong_guesses -= 1
        print("Wrong guess")
        print("Remaining chances:", wrong_guesses)

    print("Word:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)

if "_" not in display_word:
    print("You guessed the word:", secret_word)
else:
    print("Game over. The word was:", secret_word)