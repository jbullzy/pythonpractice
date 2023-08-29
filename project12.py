def integers(list):
    result = []
    for item in list:
        if isinstance(item, int) and item >= 0:
            result.append(item)
    return result


mixed_list = [10, "Hello", 25, "world", 0, "42", 7]
integer_list = integers(mixed_list)
print(integer_list)