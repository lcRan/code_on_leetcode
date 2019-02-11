def lengthOfLastWord(s):
    length = len(s)
    if length == 0:
        return 0
    length = 0
    s = s.rstrip()
    for c in s[::-1]:
        if c == ' ':
            break
        length += 1
    return length

s = "Hello World "
print (lengthOfLastWord(s))