import numpy

def oddCells(n, m, indices):
    output=0
    rowmatrix = [0]*m
    actualmatrix=[rowmatrix]*n
    actualmatrix=numpy.array(actualmatrix)
    for i in indices:
        actualmatrix[i[0]]+=1
        print(actualmatrix)
        for j in range(n):
            actualmatrix[j, i[1]]+=1
        print(actualmatrix)
    temp = [0]*n*m
    temp = numpy.array(temp)
    flatList = []
    for elem in indices:
        flatList.extend(elem)

    for i in range(len(flatList)):
        if i%2==0:
            tt = [1]*m
            #temp+=temp[i*flatList[i]:i+m-1]
    return actualmatrix

def oddCells1(n, m, indices):
    row_m = []
    col_m = []
    total = 0
    for i in indices:
        if i[0] in row_m:
            row_m.remove(i[0])
            total += len(col_m)
            total -= (m - len(col_m))
        elif i[0] not in row_m:
            row_m.append(i[0])
            total += (m - 2 * len(col_m))
        if i[1] in col_m:
            col_m.remove(i[1])
            total += len(row_m)
            total -= (n - len(row_m))
        elif i[1] not in col_m:
            col_m.append(i[1])
            total += (n - 2 * len(row_m))
    return total


def oddCells2(n, m, indices):
    row_m = []
    col_m = []
    total = 0
    for i in indices:
        if i[0] not in row_m:
            row_m.append(i[0])
            total+=(m-2*len(col_m))
        else:
            row_m.remove(i[0])
            total+=len(col_m)
            total -= (m-(len(col_m)))
        if i[1] not in col_m:
            col_m.append(i[1])
            total += (n-2*len(row_m))
        else:
            col_m.remove(i[1])
            total+=len(row_m)
            total -= (n-(len(row_m)))


    return total



n = 4
m = 5
indices = [[0, 0], [1, 0],[0,1],[0,0]]

print(oddCells(n, m, indices))
print(oddCells1(n, m, indices))
print(oddCells2(n, m, indices))