import random

words = ["apple", "tiger", "chair", "robot", "pizza"]
word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman Game")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    if all(letter in guessed for letter in word):
        print("You Win! Word was:", word)
        break
else:
    print("You Lose! Word was:", word)