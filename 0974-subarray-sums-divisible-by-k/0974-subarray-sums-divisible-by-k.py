from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        res = 0

        for num in nums:
            prefix_sum = (prefix_sum + num) % k

            if prefix_sum in prefix:
                res += prefix[prefix_sum]

            prefix[prefix_sum] += 1

        return res