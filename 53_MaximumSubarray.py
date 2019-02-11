def MaxSubarray(nums):
    if nums[0] > 0:
        newSum = nums[0]
    else:
        newSum = 0
    maxSum = nums[0]
    for num in nums[1:]:
        newSum += num
        if newSum > maxSum:
            maxSum = newSum
        if newSum < 0:
            newSum = 0

    return maxSum

nums1 = [-5, -1, -2, -3, -4]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print (MaxSubarray(nums))
print(MaxSubarray(nums1))