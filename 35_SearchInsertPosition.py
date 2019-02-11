def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        length = len(nums)
        for i in range(length):
            if target < nums[i]:
                return i
    return length

num = [1]
print (searchInsert(num,0))