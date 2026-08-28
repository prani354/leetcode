class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            curr %= k

            if curr not in d:
                d[curr] = i

            elif i - d[curr] >= 2:
                return True

        return False
        