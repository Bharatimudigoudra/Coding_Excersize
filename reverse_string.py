def reverse_string(word):
    result = ""
    for char in word:
        result = char + result
    return result

print(reverse_string("Bharati"))