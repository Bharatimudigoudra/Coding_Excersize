def palindrome(word):
    reverse= ""
    for ch in word:
        reverse = ch + reverse
    if reverse == word:
        return True
    else:
        return False

print(palindrome("Malayalam"))

