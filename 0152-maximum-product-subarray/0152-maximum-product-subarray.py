class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max , curr_min = 1 , 1
        res = nums[0]

        for num in nums:
            val = (num , num*curr_max , num*curr_min)
            curr_max , curr_min = max(val) , min(val)

            res = max(res, curr_max)

        return res