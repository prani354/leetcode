class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = [0] * n
        s = sum(nums[:k])
        res[k-1] = s
        ans = s

        for i in range(k,n):
            s += nums[i] - nums[i-k]

            res[i] = s + (0 if 0 > res[i-k] else res[i-k])

            ans = res[i] if res[i] > ans else ans

        return ans 
        