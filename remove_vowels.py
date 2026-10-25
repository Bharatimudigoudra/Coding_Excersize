"""Write def remove_vowels(s) to remove a, e, i, o, u in both small and capital letters. Keep all other characters, including spaces, unchanged.

Examples:
remove_vowels("python") → "pythn"
remove_vowels("AI Engineer") → " Engnr"
remove_vowels("xyz") → "xyz"

Use a for loop and if/else. Build the result letter by letter, without replace() or comprehensions."""

def remove_vowels(s):
    result = ""
    for char in s:
        if char not in "aeiouAEIOU":
            result += char
    return result

print(remove_vowels("python")) 