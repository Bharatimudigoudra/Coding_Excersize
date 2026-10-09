"""Write a function is_palindrome(word) that returns True if the word reads the same forwards and backwards, else False.

Examples: is_palindrome("madam") -> True, is_palindrome("hello") -> False.

Use def, a for loop and if. No slicing like word[::-1]. Hint: compare the first letter with the last, the second with the second last, and so on.
"""

def palindrome(word):
    reverse= ""
    for ch in word:
        reverse = ch + reverse
    if reverse == word:
        return True
    else:
        return False

print(palindrome("Malayalam"))

