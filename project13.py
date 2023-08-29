def doubler(string):
    result = []

    characters = list(string)

    for character in characters:
        result.append(character * 2)

    final_result = ''.join(result)

    return final_result

string = input("Give a string: ")

result = doubler(string)
print(result)