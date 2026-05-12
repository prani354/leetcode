class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max , curr_min = 0 , 0
        max_sum , min_sum = nums[0] , nums[0]
        tot_sum = 0

        for num in nums:
            curr_max = max(curr_max+num,num)
            max_sum = max(max_sum,curr_max)

            curr_min = min(curr_min+num,num)
            min_sum = min(min_sum,curr_min)

            tot_sum += num

        if max_sum < 0:
            return max_sum

        return max(max_sum,tot_sum-min_sum) #circular array so the wrap sum is quantized