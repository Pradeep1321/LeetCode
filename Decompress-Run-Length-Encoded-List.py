def decompressRLElist(nums):
    output = []
    for i in range(0,len(nums),2):
        for j in range(nums[i]):
            output.append(nums[i+1])
    return output

def decompressRLElist1(nums):
    arr = []
    for i in range(int(len(nums) / 2)):
        freq = nums[2 * i]
        value = nums[2 * i + 1]
        arr += freq * [value]
    return arr
nums = [1, 1, 2, 3,3,4]
print(decompressRLElist1(nums))