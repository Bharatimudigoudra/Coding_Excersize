"""Write a function count_words(sentence) that returns how many words are in the sentence. Words are separated by single spaces. Do not use split().
Example: count_words("I love python coding") should give 4."""

def count_words(words):
    count = 0
    for w in words:
        count = count +1
    return count

print(count_words("I love python coding"))