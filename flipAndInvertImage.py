def flipAndInvertImage(A):
    out = []
    for i in A:
        i = i[::-1]
        out.append([1-x for x in i])
    return out

A = [[1,1,0],[1,0,1],[0,0,0]]

print(flipAndInvertImage(A))