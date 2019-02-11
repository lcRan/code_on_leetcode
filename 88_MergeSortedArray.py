def MergeTwoArray(nums1, m, nums2, n):
    index = m + n - 1
    i = m - 1
    j = n - 1
    while j >= 0 :
        if i < 0:
            nums1[index] = nums2[j]
            j -= 1
        else:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
        index -= 1

nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 3, 6, 7]
nums1.extend(nums2)
MergeTwoArray (nums1,5,nums2,4)
print (nums1)