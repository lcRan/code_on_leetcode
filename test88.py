def MergeTwoArray(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while k >= 0:
        if (j < 0 or nums1[i] > nums2[j]) and i >= 0:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 3, 6, 7]
MergeTwoArray (nums1,5,nums2,4)
print (nums1)