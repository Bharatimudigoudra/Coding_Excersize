"""Rotate an array left by d positions. Elements that leave the front move to the end.

Example:
a = [1, 2, 3, 4, 5], d = 2
Result: [3, 4, 5, 1, 2]

Complete rotLeft(a, d)."""

def rotLeft(a,d):
    n = len(a)
    d = d%n # Handle cases where d is greater than n
    return a[d:]+a[:d]

print(rotLeft([1,2,3,4,5], 2))

# Time: O(n).
# Extra space: O(n), because slicing creates new lists.