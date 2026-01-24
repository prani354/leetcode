class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        i , j = 0, n - 1
        nums.sort()
        max_pair = 0

        while i < j:
            max_pair = max(max_pair,nums[i]+nums[j])
            i += 1
            j -= 1

        return max_pair


