def maxProduct(nums):
    nums.sort()
    output = lambda x : (nums[len(nums)-2]-1) * (nums[len(nums)-1]-1) if len(x)>2 else (nums[0]-1) * (nums[1]-1)
    return output(nums)

def maxProduct1(nums):
    a = 0
    b = 0
    for i in nums:
        if i >= a:
            b=a
            a=i
        elif i >= b:
            b = i

    return (a-1)*(b-1)




nums = [10,2,5,2]
print(maxProduct1(nums))