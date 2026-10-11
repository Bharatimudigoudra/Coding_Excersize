"""Write a function count_even_odd(numbers). It should return how many even numbers and how many odd numbers are in the list.
"""

def count_even_odd(nums):
    even=0
    odd=0
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1,2,3,4,5,6,7,11,12]))
