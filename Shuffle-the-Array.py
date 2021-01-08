def shuffle(nums, n):
    output=[]
    for i in range(n):
        output.append(nums[i])
        output.append(nums[i+n])
    return output

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))







