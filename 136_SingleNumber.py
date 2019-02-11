def singleNumber(nums):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] = 0
    for key, valus in dic.items():
        if valus == 0:
            return key

nums = [1, 1, 3, 4, 7, 3, 7]
print (singleNumber(nums))
