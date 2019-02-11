class Solution:
    def isPerfectSquare(self,num):
        if num < 2:
            return True
        start = 1
        end = num // 2
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > num:
                end = mid - 1
            elif mid * mid < num:
                start = mid + 1
            else:
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(4))
    print(s.isPerfectSquare(16))
    print(s.isPerfectSquare(14))