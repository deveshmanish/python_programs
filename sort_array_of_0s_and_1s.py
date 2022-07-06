def sortarray(a):
    return [0 for i in range(len(a)-sum(a))]+[1 for i in range(sum(a))]