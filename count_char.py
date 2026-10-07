"""Write a function count_chars(s) that returns how many times each character appears in the string. Use def and a for loop only.

Example:
count_chars("banana") should give {'b': 1, 'a': 3, 'n': 2}

Hint: start with an empty dictionary. For each character, if it is already in the dictionary add 1, else set it to 1."""

def count_char(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

print(count_char("Bharathi"))