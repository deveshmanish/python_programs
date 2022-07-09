def merger(a,b):
    result = []
    j = 0
    if len(b)<len(a):
        (a,b) = (b,a)
    for i in range(len(a)):
        if a[i]<b[j]:
            if not result:
                result.append(a[i])
            elif a[i]!=result[-1]:
                result.append(a[i])
        else:
            if not result:
                result.append(b[j])
            elif result and b[j]!=result[-1]:
                result.append(b[j])
            j += 1
    result += b[len(a):]
    return result