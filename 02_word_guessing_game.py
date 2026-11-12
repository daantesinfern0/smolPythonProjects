import random

word_list = ["apple", "ball", "cat", "dear", "elephant", "frolicking", "guava", "hercules", "inosuke", "jotaro"]
word = random.choice(word_list)

guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for c in word:
        if c in guessed:
            display += c
        else:
            display += "#"

    print("Word: ", display)

    if display == word:
        print("You Win!")
        break

    guess_letter = input("Guess a letter: ").lower()
    guessed.append(guess_letter)

    if guess_letter not in word:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print(f"You lost! The word was '{word}'")