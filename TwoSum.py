def Sum(GvnArry, targetamount):
    count1=0
    for iter1 in GvnArry:
        count2=count1+1
        for iter2 in GvnArry[count1+1:]:
            if iter1 + iter2 == targetamount:
                return [count1,count2]
            count2+=1
        count1+=1

    return None


print(Sum([3,2, 4],6))


