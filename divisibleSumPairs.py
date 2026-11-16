"""Given a list and a positive number k, count pairs whose sum is divisible by k. Count each pair of positions only once. Equal values at different positions count separately. Return the count, not the pairs.

python
def divisibleSumPairs(n, k, ar):
    # your code
    pass

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))  # 5
print(divisibleSumPairs(4, 5, [1, 2, 3, 4]))        # 2
print(divisibleSumPairs(4, 4, [2, 2, 2, 2]))        # 6
print(divisibleSumPairs(3, 10, [1, 2, 4]))          # 0


n is the length of ar. Use loops first. Don't sort or change the list."""

def divisibleSumPairs(n,k,ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))

# Time: O(n²), because you check every pair.
# Extra space: O(1), because you only keep a counter.