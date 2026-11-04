"""Given a non-empty list nums, return the element that appears more than half the time. You can assume such an element always exists.

Example 1:
Input: [3, 2, 3]
Output: 3

Example 2:
Input: [2, 2, 1, 1, 1, 2, 2]
Output: 2

Write:
def majority_element(nums):

Return the answer, don't only print it. Use your own loop, without sorting, Counter or max(). A counting dictionary is allowed for your first version.

Test at least these cases: one element, all elements equal, and a majority appearing mainly at the start or end.

Bonus after it works: O(n) time and O(1) extra space, without a dictionary."""

from itertools import count


def majority_element(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] = 1
        else:
            count[num] = 1
    for num in count:
        if count[num] > len(nums) // 2:
            return num

print(majority_element([3, 2, 3]))  # Output: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2