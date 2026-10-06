"""def remove_duplicate_chars(word):
    # keep only chars that appear exactly once
    result = ""
    for ch in word:
        if word.count(ch) == 1:
            result += ch
    return result

print(remove_duplicate_chars("abbaCa")) # Output: Ca"""


def remove_duplicates_keep_first(word):
    result = ""
    for ch in word:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates_keep_first("abbaCa")) # Output: abC


"""Remove adjacent duplicates from a string. For example, "abbaca" becomes "ca" because "bb" and "aa" are removed. Used stack here to keep track of the characters.

def remove_adjacent(s: str) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop() # adjacent duplicate found, remove both
        else:
            stack.append(ch)
    return "".join(stack)

print(remove_adjacent("abbaca")) # ca
print(remove_adjacent("azxxzy")) # ay

"""