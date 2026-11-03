"""Write this function:

def move_zeroes(nums):

Move all zeroes to the end of the same list. Keep the other numbers in their original order. Change the list directly; don't return a new list.

Examples:
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
[0, 0, 1] → [1, 0, 0]
[1, 2, 3] → [1, 2, 3]
[0] → [0]

Rules: no sorting or second list. Aim for O(n) time and O(1) extra space.

Hint: keep a position for where the next non-zero number should go."""

def move_zeroes(nums):
    next_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_non_zero] = nums[i]
            next_non_zero += 1
    while next_non_zero < len(nums):
        nums[next_non_zero] = 0
        next_non_zero += 1

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)