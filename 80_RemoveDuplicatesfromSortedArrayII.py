class Solution:
    def removeDuplicates(self,nums):
        flag = 0
        length = len (nums)
        i = length - 1
        while i > 0:
            if flag == 1 and nums[i] == nums[i - 1]:
                del nums[i]
            elif nums[i] == nums[i - 1]:
                flag = 1
            else:
                flag = 0
            i -= 1
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    nums1 = [1]
    print(s.removeDuplicates(nums))
    print(s.removeDuplicates(nums1))