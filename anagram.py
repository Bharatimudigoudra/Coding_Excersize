"""Write a function:
def is_anagram(a, b):

Return True if both words contain the same letters with the same counts, otherwise False. Assume lowercase English letters; no spaces.

Examples:
"listen", "silent" → True
"rat", "car" → False
"aab", "abb" → False
"abc", "abcd" → False
"", "" → True

Use def, loops and dictionaries. Don't use sorted(), sort(), slicing or comprehensions."""

def is_anagram(a,b):
    if len(a)!=len(b):
        return False
    count_a = {}
    for letter in a:
        if letter in count_a:
            count_a[letter] += 1
        else:
            count_a[letter] = 1
    count_b = {}
    for letter in b:
        if letter in count_b:
            count_b[letter] += 1
        else:
            count_b[letter] = 1
    return count_a == count_b

print(is_anagram("listen", "silent")) # True
print(is_anagram("car", "rat")) # False
print(is_anagram("aab", "abb")) # False