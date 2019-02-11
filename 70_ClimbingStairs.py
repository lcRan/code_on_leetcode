def climbStairs(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))