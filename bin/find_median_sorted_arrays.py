class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1.sort()
        num_len = len(nums1)
        mid = int(num_len/2)
        if num_len%2==0:
            return (nums1[mid]+nums1[mid-1])/2
        else:
                return nums1[mid]
