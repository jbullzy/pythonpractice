# Palindrome Checker

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def palindrome(word):
    word = word.lower()
    r = reverse(word)
    s = word

    if s == r:
        return True

    else:
        return False



s = input("Check if your word is a palindrome: ")

print(s)

r = reverse(s)

print(r)


result = palindrome(s)
print(result)