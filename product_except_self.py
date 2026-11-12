"""November 12 coding exercise: Product of Array Except Self

Write product_except_self(nums).
Return a new list where result[i] is the product of every number in nums
except nums[i]. Do not change nums.

Example: [1, 2, 3, 4] -> [24, 12, 8, 6]
The first result is 2 * 3 * 4 = 24; the second is 1 * 3 * 4 = 12.

Rules:
- Input contains at least two integers. Zeros and negatives are allowed.
- Do not use division, including //, or an imported product helper.
- Aim for O(n) time. Extra lists are allowed on the first attempt.
- Bonus: O(1) extra space, excluding the returned list.

Try it yourself first. Send your code in chat for testing and a score.
Also explain how your code finds 8 at index 2 of [1, 2, 3, 4].
"""


def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    # Left product
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    # Right product
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res   


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 1, 2, 3], [6, 0, 0, 0]),
        ([0, 0, 2], [0, 0, 0]),
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),
        ([5, 2], [2, 5]),
    ]
    for nums, expected in tests:
        original = nums.copy()
        actual = product_except_self(nums)
        status = "PASS" if actual == expected and nums == original else "TRY AGAIN"
        print(f"{status}: input={original}, result={actual}, expected={expected}")
        if nums != original:
            print("Keep the input list unchanged.")
