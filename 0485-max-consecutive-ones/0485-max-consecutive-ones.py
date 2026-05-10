class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones = 0
        left = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                left = right + 1

            curr_length = right - left + 1
            max_ones = max(max_ones,curr_length)

        return max_ones