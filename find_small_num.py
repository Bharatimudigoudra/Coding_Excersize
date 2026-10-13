"""Write a function find_smallest(numbers) that returns the smallest number in a non-empty list.

Examples:
[6, 3, 9, 2, 8] → 2
[-4, 0, -9, 5] → -9
[7] → 7

Use def, a for loop and if. No min(), sorting or comprehensions.

Hint: start with the first number as the smallest so far.
"""

def find_smallest(num):
    n = num[0]
    for i in num:
        if i < n:
            n = i
    return n

print(find_smallest([6,3,9,2,8]))
