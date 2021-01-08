def subtractProductAndSum(n) :
    sum = 0
    product = 1
    while n >0:
        product= n%10 * product
        sum = n%10 + sum
        n=n//10
    return product - sum

n=705
print(subtractProductAndSum(n))
