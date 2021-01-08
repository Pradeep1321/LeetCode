def median( num1,num2):
    mixed = sorted((num1)+(num2))
    median = lambda x: [x[len(x)//2],x[(len(x)//2)-1]] if len(x)%2 == 0 or len(x)==3 else  [x[len(x)//2]]
    return sum(median(mixed))/len(median(mixed))


if __name__ == '__main__':
    a = []
    b = [1]
    print(median(a,b))