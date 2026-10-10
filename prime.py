"""Write a function is_prime(n) that returns True if n is a prime number, else False. Use def and a for loop only.
Examples: is_prime(7) is True, is_prime(8) is False, is_prime(1) is False."""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(15))