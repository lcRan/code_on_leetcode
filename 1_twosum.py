def twoSum (nums, target):
    arr = {}
    length = len(nums)
    for i in range (length):
        if (target - nums[i]) in arr:
            return [arr[target - nums[i]], i]
        arr[nums[i]] = i;

nums = [1,2,5,6,9]
print (twoSum(nums,7))

