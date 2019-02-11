def plusOne(digits):
    plus = 1
    for i in range(len(digits))[::-1]:
        digits[i] += plus
        if digits[i] == 10:
            digits[i] -= 10
            plus = 1
        else:
            plus = 0
    if plus == 1:
        digits.insert(0,1)
    return digits

nums = [9, 9]
print (plusOne(nums))