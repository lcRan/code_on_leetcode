def addBinary (a,b):
    i, m, n, result, carry = 1, len(a), len(b), [], 0
    while i <= m or i <= n:
        temp = carry
        if i <= m:
            temp  += int(a[-i])
        if i <= n:
            temp += int(b[-i])

        carry = temp // 2
        result.append(str(temp % 2))
        i += 1

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])

a = "11"
b = "1"
print (type (addBinary(a,b)))
print (addBinary(a,b))

