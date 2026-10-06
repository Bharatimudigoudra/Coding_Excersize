"""Write a Python function that takes a list of numbers and returns the second largest number.
Example: [4, 9, 2, 9, 7] gives 7."""

def second_largest(numbers):
    largest = 0
    second = 0
    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    return second

print(second_largest([4, 9, 2, 9, 7]))