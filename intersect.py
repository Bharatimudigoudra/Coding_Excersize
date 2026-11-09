"""Given two lists, return the numbers present in both. Keep each number only as many times as it appears in BOTH lists.

Examples:
intersect([1, 2, 2, 1], [2, 2]) → [2, 2]
intersect([2, 2, 2], [2]) → [2]
intersect([4, 9, 5], [9, 4, 9, 8, 4]) → [4, 9]
intersect([1, 2], [3, 4]) → []

Any result order is fine. Try with loops and a dictionary, without sorting or Counter.

Starter:

def intersect(nums1, nums2):
    # Your code here
    pass

print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([2, 2, 2], [2]))
print(intersect([], [1, 2]))"""

def intersect(num1, num2):
    result = []
    count = {}

    for i in num1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in num2:
        if i in count and count[i] > 0:
            result.append(i)
            count[i] -= 1

    return result

print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([2, 2, 2], [2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 2], [3, 4]))
print(intersect([], [1, 2]))
