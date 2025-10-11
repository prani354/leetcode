class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        arr = sorted(counter.keys())
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            val = arr[i] * counter[arr[i]]
            j = i - 1

            while j >= 0 and arr[i] - arr[j] <= 2:
                j -= 1

            dp[i] = max(dp[i-1] if i > 0 else 0, val + (dp[j] if j >= 0 else 0))

        return dp[-1]