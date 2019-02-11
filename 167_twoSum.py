def twoSum(numbers, target):
    arr = {}
    length = len (numbers)
    for i in range (length):
        if (target - numbers[i]) in arr:
            return [arr[target - numbers[i]]+1,i+1]
        else:
            arr[numbers[i]] = i

nums = [1,2,5,6,9]
print (twoSum(nums,7))