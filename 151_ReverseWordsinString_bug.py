def reverseWords(self, s):
    s_list = list(s)
    i = 0
    length = len(s_list)
    while i < length:
        if s_list[i] != ' ':
            start = i
            end = start + 1
            while (end < length) and s_list[end] != ' ':
                end += 1
            i = end
            end -= 1
            while start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1

        else:
            i += 1
    return ''.join(s_list)

s = 'the sky  is blue '
s = reverseWords(s)

print(''.join(s))


