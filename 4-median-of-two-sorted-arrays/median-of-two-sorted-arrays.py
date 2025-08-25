class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        k = len(nums3)
        mid = k//2
        if k % 2 == 0:
            return (nums3[mid-1] + nums3[mid]) /2
        else:
            return nums3[mid]
