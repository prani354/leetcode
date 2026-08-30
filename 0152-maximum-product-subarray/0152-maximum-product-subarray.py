class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max , curr_min = 1 , 1
        res = nums[0]

        for num in nums:
            value = (num,curr_min*num,curr_max*num)
            curr_max,curr_min = max(value),min(value)
            res = max(curr_max,res)

        return res
        