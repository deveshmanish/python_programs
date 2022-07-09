def findSubString(sampleString, subString):
    j = 0
    for i in range(len(sampleString)):
        if subString[j] == sampleString[i]:
            j += 1
            if j == len(subString) - 1:
                return True

    return False
