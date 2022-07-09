def printMatrixWave(array):
    flag = True
    for j in range(len(array[0])):
        for i in range(len(array)) if flag else range(len(array)-1,0,-1):
            print(array[i][j],end=' ')
        flag = not flag