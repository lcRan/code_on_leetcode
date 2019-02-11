

# A -> 1 B -> 2 ... Z -> 26
# AA -> 27
def titleToNumber(s):
    result = 0
    n = len(s)
    for i in range(n):
        # ord() 返回对应字母的ASCII
        # ord('a') --- 97  ord('b') --- 98
        result = result * 26 + ord(s[i]) - 64

    return result


# print(ord('A'))   65
if __name__ == '__main__':
    s1 = "A"
    s2 = "AB"
    s3 = "ZY"
    print(titleToNumber(s1))
    print(titleToNumber(s2))
    print(titleToNumber(s3))
