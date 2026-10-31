"""Longest Substring Without Repeating Characters

Write length_of_longest_substring(s). Return the length of the longest continuous part of the string with no repeated character. Treat uppercase and lowercase as different characters; spaces count too.

Examples:
* "abcabcbb" → 3 ("abc")
* "bbbbb" → 1
* "pwwkew" → 3 ("wke", not "pwke" because it isn't continuous)
* "abba" → 2
* "" → 0

Aim for one pass through the string. Add short comments explaining your code. Send your attempt here; I'll test the edge cases and score it out of 10."""

def length_of_longest_substring(s):
    char_index_map = {}
    start = 0
    max_length = 0
    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
            char_index_map[char] = i
        else:
            char_index_map[char] = i
            max_length = max(max_length, i - start + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))
