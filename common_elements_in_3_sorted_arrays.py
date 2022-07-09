'''Write a program to find common element in 3 sorted arrarys with O(n) time complexity and no extra space'''


def commonElements(a, b, c):
    common = []
    index_a, index_b, index_c = 0, 0, 0
    while (index_a < len(a) and index_b < len(b) and index_c < len(c)):
        if a[index_a] == b[index_b] and a[index_a] == c[index_c]:
            common.append(a[index_a])
            (index_a, index_b, index_c) = (index_a + 1, index_b + 1, index_c + 1)
        elif a[index_a] == c[index_c] and a[index_a] > b[index_b]:
            index_b += 1
        elif b[index_b] == c[index_c] and b[index_b] > a[index_a]:
            index_a += 1
        elif a[index_a] == b[index_b] and a[index_a] > c[index_c]:
            index_c += 1
        elif a[index_a] > b[index_b] and a[index_a] > c[index_c]:
            (index_b, index_c) = (index_b + 1, index_c + 1)
        elif b[index_b] > a[index_a] and b[index_b] > c[index_c]:
            (index_a, index_c) = (index_a + 1, index_c + 1)
        elif c[index_c] > a[index_a] and c[index_c] > b[index_b]:
            (index_a, index_b) = (index_a + 1, index_b + 1)
    return common
