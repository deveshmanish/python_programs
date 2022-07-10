def checkPalindrome(number):
    binary = "{0:b}".format(int(number))
    (i, j) = (0, len(binary) - 1)
    while binary[j] == '0':
        j -= 1
    while j >= i:
        if binary[i] == binary[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
