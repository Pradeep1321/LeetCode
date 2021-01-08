import random
def sumZero(n) :
    arr = [];
    if (n % 2 != 0):
        arr.append(0);
    j = 1;
    while len(arr) < n:
        i = n - j;
        arr.append(i);
        arr.append(-i);
        j += 1;
    return arr;
print(sumZero(5))