def numIdenticalPairs1(nums) :
    output=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                output=output+1
    return output

def numIdenticalPairs(nums):
        d = {}
        for n in nums:
            d[n] = d.setdefault(n, 0) + 1
        r = 0
        for value in d.values():
            r += get_good_pairs(value)
        return r

def get_good_pairs(amount):
        return amount * (amount - 1) // 2

nums = [1,2,3,1,1,3,1,1]
print(numIdenticalPairs(nums))
print("=====")
print(numIdenticalPairs1(nums))