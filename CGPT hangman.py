import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "flamingo"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\nCurrent word:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
                if attempts == 0:
                    print("Sorry, you're out of attempts. The word was:", word_to_guess)
                    break
            else:
                if set(guessed_letters) >= set(word_to_guess):
                    print("Congratulations! You've guessed the word:", word_to_guess)
                    break

hangman()
