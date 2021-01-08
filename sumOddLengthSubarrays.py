def sumOddLengthSubarrays(arr):
    sum=0
    j=1
    while j <= len(arr):
        for i in range(len(arr)-(j-1)):
            subarr = arr[i:i + j]
            for l in range(len(subarr)):
                sum+=subarr[l]
        j+=2
    return sum


arr = [1, 4, 2, 5, 3]
print(sumOddLengthSubarrays(arr))


