def selfDividingNumbers(left,right):
    out = []
    for i in range(left, right + 1):
        j = i
        for m in str(j):
            if int(m) != 0 and i > 9:
                if i % int(m) != 0:
                    i = 0
                    break
            elif int(m) == 0:
                i = 0
        if i == j:
            out.append(i)
    return out

print(selfDividingNumbers(1,22))