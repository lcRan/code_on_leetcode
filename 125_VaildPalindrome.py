def isPalindrome(s):
    length = len(s)
    start = 0
    end = length - 1
    if length == 0 or length == 1:
        return True
    while start < end:
        while not s[start].isalnum() and start < end:
            #print ("s[start]:",s[start])
            start += 1
        while not s[end].isalnum() and start < end:
            #print ("s[end]:",s[end])
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "09"
print (isPalindrome(s1))
print (isPalindrome(s2))
print (isPalindrome(s3))