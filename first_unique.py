"""def first_unique(text)

Return the first character that appears only once. Return None if none exists.

"swiss" → "w"
"aabbc" → "c"
"aabb" → None
"abc" → "a"
"" → None

Use def, loops and a dictionary. No imports, comprehensions or count(). Return Python None, not the string "None"."""

def first_unique(text):
    count = {}
    for letter in text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

print(first_unique("swiss")) # "w"
