import math
def diagonalSum(mat):
    sum=0
    for i in range(len(mat)):
        sum+=mat[i][i]
    j=0
    for i in range(len(mat)-1, -1, -1):
        if i == (len(mat) // 2) and (len(mat) % 2 != 0) :
            j=j+1
            continue
        sum += mat[j][i]
        j+=1
    return sum

def sumoftwonumbers(lt,target):
    for i in lt:
        if (target - i) in lt[lt.index(i)+1:]:
            print("{} and {} are pairs found".format(i,target-i))
            return (i,(target-i))
    return ("No Pairs found")

mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]

print(diagonalSum(mat))


lt = [2]
target = 4
print(sumoftwonumbers(lt,target))