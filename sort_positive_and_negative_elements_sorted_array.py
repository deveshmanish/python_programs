def sortArray(a):
    i = 0
    for j in range(len(a)-1,i,-1):
        if abs(a[i])<=abs(a[i+1]):
            (a[i], a[i + 1]) = (a[i + 1], a[i])
        if abs(a[i])>=abs(a[j]):
            (a[i],a[j]) = (a[j],a[i])
    return a