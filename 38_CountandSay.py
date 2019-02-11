class Solution:
    def countAndSay(self, n):
        s = ['1']
        length = 1
        while n > 1:
            n -= 1
            i = 0
            result = []
            while i < length:
                num = 1
                while i + 1 < length and s[i+1] == s[i]:
                    num += 1
                    i += 1

                result.append(str(num))
                result.append(s[i])
                i += 1
            s = result
            length = len(result)

        return ''.join(s)

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(2))
    print(solution.countAndSay(3))
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))