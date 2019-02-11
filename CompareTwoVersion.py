

# 请用您熟悉的编程语言，编程实现一个比较任意两个软件版本号大小的函数，
# 如 1.2.3a 和 1.2.4b 比较，后者版本号更大，请考虑各种情况，不可以使用系统提供的比较函数。


def compare_two_version(version1, version2):
    v1 = version1.lower()
    v2 = version2.lower()
    list1 = v1.split('.')
    list2 = v2.split('.')
    len1 = len(list1)
    len2 = len(list2)
    if len1 < len2:
        max_len = len2
        diff_len = len2 - len1
        for i in range(diff_len):
            list1.append('0')
    else:
        max_len = len1
        diff_len = len1 - len2
        for i in range(diff_len):
            list2.append('0')
    for i in range(max_len):
        if list1[i] == list2[i]:
            pass
        elif list1[i] > list2[i]:
            return 1
        else:
            return -1
    return 0


v1 = '01.2.3'
v2 = '1.2.3'
print(compare_two_version(v1, v2))