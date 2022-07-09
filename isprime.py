import math


# Check if a number(n) is prime or not
def isprime(n):
    # There are no prime numbers below 2
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    elif (n == 2 or n == 3):
        return True
    # any mulitple of 2 and 3 will not be a composite number
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    # If n is composite, its smallest nontrivial divisor does not exceed √n
    # Numbers that are not divisible by 2 or 3 will be of the form 6*k ± 1
    for i in range(5, math.floor(math.sqrt(n)) + 1, 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
    return True
