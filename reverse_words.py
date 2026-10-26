"""Write def reverse_words(sentence) using a for loop. Keep the letters inside each word unchanged.

Examples:
reverse_words("I love python") → "python love I"
reverse_words("AI engineer") → "engineer AI"
reverse_words("hello") → "hello"

You can use split() to get the words."""

def reverse_words(s):
    words = s.split()
    result = ""
    for i in range(len(words) -1, -1, -1):
        result += words[i] + " "
    return result.strip()

print(reverse_words("I Love Python"))