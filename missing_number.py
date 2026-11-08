"""A list contains n distinct numbers from 0 to n. Exactly one number is missing. Return it.

Examples:
missing_number([3, 0, 1]) → 2
missing_number([0, 1]) → 2
missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) → 8

Complete this:

def missing_number(nums):
    # Your code here
    pass

print(missing_number([3, 0, 1]))

Also test [0] → 1 and [1] → 0. Try without sorting."""

def missing_number(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i

print(missing_number([3,0,1]))