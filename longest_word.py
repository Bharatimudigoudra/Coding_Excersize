"""Write a function longest_word(sentence) using def and a loop. Return the longest word. If two words have the same length, return the first. For an empty sentence, return an empty string.

Test cases:
"I love Python programming" → "programming"
"cat dog bat" → "cat"
"" → ""

Use split() and len(), but not max()."""

def longest_word(sentence):
    words = sentence.split()
    longest = "" 
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("I love python programming"))

