"""Return the largest sum from a continuous part of a list. You must take at least one number. The list will not be empty.

Examples:
[1, -2, 3, 4, -1] → 7 (3 + 4)
[-3, -1, -2] → -1
[5] → 5

Use a function and loops. Don't sort the list. A simple working solution is fine first.

Start with:
def max_subarray(nums):
    # your code here
    pass"""

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([1,-2,3,4,-1]))