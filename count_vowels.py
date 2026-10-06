"""Write a function count_vowels(text) that returns how many vowels (a, e, i, o, u) are in the text. Example: count_vowels("zeroqueue") gives 5.
Use def and a for loop only."""

def count_vowels(s):
    vowels = "AEIOUaeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("zeroqueue"))