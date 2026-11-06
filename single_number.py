"""Given a non-empty list, every number appears twice except one. Return that single number.

Examples:
[2, 2, 1] → 1
[4, 1, 2, 1, 2] → 4
[1] → 1

Write:
def single_number(nums):

Use your own loop without sorting or Counter. A dictionary is allowed. Return the answer, don't only print it."""

def single_number(nums):
    n = {}
    for i in nums:
        if i in n:
            n[i] += 1
        else:
            n[i] = 1

    for i in n:
        if n[i] == 1:
            return i

print(single_number([2, 2, 1]))