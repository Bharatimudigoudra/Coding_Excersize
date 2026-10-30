"""Write two_sum(nums, target) to return the indices of two numbers that add up to target.

Rules:
* Indices start at 0.
* Don't use the same list position twice.
* Each input has exactly one valid pair. Return its indices in either order.

Examples:
two_sum([2, 7, 11, 15], 9) → [0, 1]
two_sum([3, 2, 4], 6) → [1, 2]
two_sum([3, 3], 6) → [0, 1]
two_sum([-3, 4, 3, 90], 0) → [0, 2]

First make it work. Then try to avoid checking every possible pair. Explain your time complexity too."""

def two_sums(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return None

print(two_sums([2,7,11,15,9], 9))

# complexity explanation: average time O(n), extra space O(n). 
# Dictionary lookup is O(1) on average, and you scan the list once.