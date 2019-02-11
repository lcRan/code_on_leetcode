def longestCommonPrefix(strs):
    length = len(strs)
    if length == 0:
        return ""
    com = strs[0]
    min = len (strs[0])
    for i in range (1,len(strs)):
        j = 0
        while j < len(strs[i]) and j < min:
            if com[j] != strs[i][j]:
                break
            j += 1
        min = j
    return com[:min]

strs = ["string","string123","str2","stri"]
print (len (strs))
com = longestCommonPrefix(strs)
print (com)