class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        res = nums + nums
        print(res)

        ones = sum(nums)
        curr_ones = max_ones = sum(nums[:ones])

        for i in range(ones,len(res)):
            curr_ones += res[i] - res[i-ones]
            max_ones = max(max_ones,curr_ones)

        return ones - max_ones