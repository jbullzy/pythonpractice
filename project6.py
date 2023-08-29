# Counting the vowels in a string

thestring = input("Enter some words with vowels: ")

def countvowels(somestring):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in somestring:
        if char in vowels:
            vowel_count += 1

    return vowel_count

vowel_count = countvowels(thestring)

print(f"That contains {vowel_count} vowels")