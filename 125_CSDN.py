class Solution():
    def isPalindrome(self,s):
        s = s.lower()
        string = []
        for c in s:
            if c.isalnum():
                string.append(c)
        i, j = 0, len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == "__main__":
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = "09"

    print (solution.isPalindrome(s1))
    print (solution.isPalindrome(s2))
    print (solution.isPalindrome(s3))

