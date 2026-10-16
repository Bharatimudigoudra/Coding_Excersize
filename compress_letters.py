"""def compress_runs(text)

Replace each consecutive group of the same letter with that letter and its count. Count separate groups separately.

"aabccc" → "a2b1c3"
"aaa" → "a3"
"abc" → "a1b1c1"
"aba" → "a1b1a1"
"" → ""

Assume lowercase English letters. Use def, a loop and if/else. No imports, comprehensions or count().
"""
def compress_letters(text):
    if not text:
        return ""
    compresses = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compresses += text[i-1] + str(count)
            count = 1
        compresses += text[-1] + str(count)
    return compresses

print(compress_letters("aabccc")) # "a2b1c3"
print(compress_letters("aaa")) # "a3"    