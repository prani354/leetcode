class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dp(J, K, i, s):
            if J < 0 or K< 0 or J + s.bit_count() < K:
                return 0
            if J == 0:
                if K == s.bit_count():
                    return 1
                else:
                    return 0
            if i >= len(nums):
                return 0
            res = 0
            for q in range(J + 1):
                tmp = comb(J, q) * pow(nums[i], q, mod) % mod
                f = s + q
                res += tmp * dp(J - q, K - f % 2, i + 1, f // 2)
            return res % mod
        return dp(m, k, 0, 0)