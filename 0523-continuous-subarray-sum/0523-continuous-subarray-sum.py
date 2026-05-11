class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sum %= k

            if prefix_sum not in d:
                d[prefix_sum] = i

            elif i - d[prefix_sum] >= 2:
                return True

        return False