'''
两个数的除法，不能使用乘、除、模运算
通过移位解决乘法问题

'''


class Solution():
    def divide(self, diviend, divisor):
        MAX_INT = 2147483647
        sign = 1 if (diviend > 0 and divisor > 0) or (diviend < 0 and divisor < 0) \
            else -1
        quotient = 0
        diviend = abs(diviend)
        divisor = abs(divisor)
        while diviend >= divisor:
            k = 0
            tmp = divisor
            while diviend >= tmp:
                diviend -= tmp
                quotient += 1 << k
                tmp <<= 1
                k += 1
        quotient = sign * quotient
        if quotient > MAX_INT:
            quotient = MAX_INT
        return quotient

if __name__ == '__main__':
    s = Solution()
    result = []
    result.append(s.divide(7, 3))
    result.append(s.divide(10, -2))
    result.append(s.divide(15, 2))
    print(result)
