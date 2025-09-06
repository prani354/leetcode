class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        if len(nums) % 2 != 0:
            return float(nums[len(nums)//2])

        else:
            mid = len(nums) // 2
            value = (nums[mid] + nums[mid-1]) / 2
            return float(value)

    