"""A staircase has n steps. Each time, you can climb either 1 step or 2 steps. Find how many different ways you can reach the top.

Example 1:
Input: n = 2
Output: 2
Ways: 1+1 or 2

Example 2:
Input: n = 3
Output: 3
Ways: 1+1+1, 1+2 or 2+1

Example 3:
Input: n = 5
Output: 8

Write climb_stairs(n) to return the number of ways. Assume n is always at least 1."""

def claim_stairs(n):
    result = {}
    result[1] = 1
    result[2] = 2

    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]

print(claim_stairs(5))  # 8
        