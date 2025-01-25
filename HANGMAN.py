import random
import os

def get_word():
    words = ["apple", "mango", "orange", "grape", "banana", "pineapple", "strawberry", "blueberry", "kiwi"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_hangman(attempts):
    stages = [
        """
           +---+
               |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return stages[6 - attempts]

def display_game_over():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========

        ###############################
        #                             #
        #          GAME OVER          #
        #                             #
        ###############################
    """)

def hangman():
    print("Welcome to Hangman!")
    word = get_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\n" + display_hangman(attempts))
        print("Word:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter (or press 'q' to quit): ").lower()
        
        if guess == 'q':
            print("You exited the game. Goodbye!")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                return
        else:
            print("Wrong guess!")
            attempts -= 1

    display_game_over()
    print("The word was:", word)

if __name__ == "__main__":
    hangman()
