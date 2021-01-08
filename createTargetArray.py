def createTargetArray(nums, index):
    output = []
    for i in range (len(nums)):
            output.insert(index[i],nums[i])
    return output

nums = [0,1,2,3,4]
index = [0,1,2,2,1]

print(createTargetArray1(nums,index))

