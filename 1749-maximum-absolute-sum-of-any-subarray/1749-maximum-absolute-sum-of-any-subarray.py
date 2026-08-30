class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max = 0
        curr_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        res = 0

        for num in nums:
            curr_max = max(curr_max+num,num)
            max_sum = max(max_sum,curr_max)
            curr_min = min(curr_min+num,num)
            min_sum = min(min_sum,curr_min)

        print(max_sum,min_sum)
        
        return max(abs(max_sum),abs(min_sum))