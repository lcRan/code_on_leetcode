
list = []
for x in range(1, 10):
    list2 = []
    for y in range(1, x + 1):
        list2.append('%s*%s=%-2s' % (y, x, x * y))
    list.append(' '.join(list2))
# print('\n'.join(list))
# 一句话输出 9 * 9 乘法表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y)
                           for y in range(1, x+1)]) for x in range(1, 10)]))
