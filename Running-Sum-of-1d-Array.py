def runningSum(nums):
    runSum = []
    for i in range(len(nums)):
        if i == 0:
            runSum.append(nums[i])
        else:
            runSum.append(runSum[i-1]+nums[i])
    return runSum


print(runningSum([1,2,3,4]))
