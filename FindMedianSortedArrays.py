class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        num_len = len(nums1)
        if num_len == 0:
            return
        elif num_len == 1:
            return nums1[0]
        else:
            mid = int(num_len/2)
            if num_len%2==0:
                return (nums1[mid]+nums1[mid-1])/2
            else:
                return nums1[mid]
