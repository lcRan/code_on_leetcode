class Solution:
    def mySqrt(self,x):
        if x < 2:
            return x
        start = 1
        end = x // 2
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
                lastmid = mid
            else:
                return mid
        return lastmid


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(2))
    print(s.mySqrt(4))
    print(s.mySqrt(8))
    print(s.mySqrt(255))