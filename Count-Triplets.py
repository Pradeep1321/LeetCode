from itertools import *
def countGoodTriplets(arr, a, b, c):
    count = 0
    temp = []
    for i in combinations(arr,3):
        temp.append(i)
    for i in temp:
        if abs(i[0]-i[1])<=a and abs(i[1]-i[2])<=b and abs(i[0]-i[2])<=c:
            count+=1
    return count


arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))
