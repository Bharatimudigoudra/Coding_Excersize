#Find the length of the longest substring without repeating characters

def length_of_longest(s):
    last = {} # char -> most recent index
    start = best = 0
    for i, c in enumerate(s):
        if c in last and last[c] >= start:
            start = last[c] + 1
        last[c] = i
        best = max(best, i - start + 1)
    return best

"""
def length_of_longest(s):
    best = ""
    for start in range(len(s)):
        seen = []
        current = ""
        for end in range(start, len(s)):
            ch = s[end]
            if ch in seen:
                break
            seen.append(ch)
            current = current + ch
        if len(current) > len(best):
            best = current
    return len(best)
"""

print(length_of_longest("abcdefgabsd"))