class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        max_idx = 0

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_idx = i

        return max_idx

