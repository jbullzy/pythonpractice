def hangman(): 
    word = "Palindrome"
    blanks = "_" * len(word)

    print(blanks)
    print("Okay, guess a letter:")

    guess = input()

    if guess in word:
        print("Correct")

    else:
        print("incorrect")

    



hangman()