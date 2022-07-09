import isprime


def nthprime(n):
    if (n < 2):
        return 2
    elif (n == 2):
        return 3
    else:
        i = 5
        while (n > 2):
            if isprime.isprime(i):
                n = n - 1
            i = i + 1
        return i - 1
