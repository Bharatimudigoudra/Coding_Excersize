"""Write contains_duplicate(nums). Return True if any number repeats, otherwise False.

[1, 2, 3, 1] → True
[1, 2, 3, 4] → False
[] → False
[7] → False

Use one loop and a dictionary. No set(), count() or sorting. Aim for O(n)."""

def contains_duplicate(nums):
    seen = {}
    for i in nums:
        if i in seen:
            return True
        seen[i] = 1
    return False

print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False