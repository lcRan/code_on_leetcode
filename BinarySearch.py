

# 当 x 不存在时，返回相应位置，不存在时，返回 -1
def binary_search(sorted_list, x):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == x:
            return mid
        elif sorted_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# 当 x 不存在时，返回相应位置，不存在时，返回 -1
# 递归
def binary_search1(sorted_list, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if sorted_list[mid] == x:
        return mid
    elif sorted_list[mid] < x:
        return binary_search1(sorted_list, x, mid + 1, end)
    else:
        return binary_search1(sorted_list, x, start, mid - 1)


# 当 x 不存在时，返回相应位置，不存在时，返回该插入的位置
def binary_search2(sorted_list, x):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == x:
            return mid
        elif sorted_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start


# 当 x 不存在时，返回相应位置，不存在时，返回该插入的位置
# 递归
def binary_search3(sorted_list, x, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if sorted_list[mid] == x:
        return mid
    elif sorted_list[mid] < x:
        return binary_search3(sorted_list, x, mid + 1, end)
    else:
        return binary_search3(sorted_list, x, start, mid - 1)


if __name__ == '__main__':
    sorted_list = [1, 2, 4, 5, 8]
    start = 0
    end = len(sorted_list) - 1
    result = []

    # 非递归
    result.append(binary_search(sorted_list, 1))
    result.append(binary_search(sorted_list, 4))
    result.append(binary_search(sorted_list, 6))
    result.append(binary_search(sorted_list, 8))
    print(result)
    # 递归
    result1 = []
    result1.append(binary_search1(sorted_list, 1, start, end))
    result1.append(binary_search1(sorted_list, 4, start, end))
    result1.append(binary_search1(sorted_list, 6, start, end))
    result1.append(binary_search1(sorted_list, 8, start, end))
    print(result1)

    result2 = []
    result2.append(binary_search2(sorted_list, 0))
    result2.append(binary_search2(sorted_list, 4))
    result2.append(binary_search2(sorted_list, 6))
    result2.append(binary_search2(sorted_list, 9))
    print(result2)

    result3 = []
    result3.append(binary_search3(sorted_list, 0, start, end))
    result3.append(binary_search3(sorted_list, 4, start, end))
    result3.append(binary_search3(sorted_list, 6, start, end))
    result3.append(binary_search3(sorted_list, 9, start, end))
    print(result3)
