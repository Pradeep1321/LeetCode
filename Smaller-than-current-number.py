def smallerNumbersThanCurrent(nums):
    out = []
    temp = nums.copy()
    nums.sort()
    for i in range(len(nums)):
        out.append(nums.index(temp[i]))
    return out
def smallerNumbersThanCurrent1(nums):
    t = sorted(nums)
    m = {}
    for i in range(len(t)):
        if t[i] not in m:
            m[t[i]] = i
    print(m)
    return [m[i] for i in nums]
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent1(nums))