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
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(claim_stairs(5))  # 8
        