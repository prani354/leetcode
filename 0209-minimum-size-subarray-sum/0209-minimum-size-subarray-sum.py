class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)
        left = 0
        curr_sum = 0

        if sum(nums) < target:
            return 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length,right-left+1)
                curr_sum -= nums[left]
                left += 1

            
               

        return min_length                


        


        