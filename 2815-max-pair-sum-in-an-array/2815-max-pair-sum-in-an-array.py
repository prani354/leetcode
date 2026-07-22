from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        freq = defaultdict(list)

        for num in nums:
            max_num = int(max(str(num)))
            freq[max_num].append(num)

        ans = -1
        for num in freq:
            if len(freq[num]) > 1:
                freq[num].sort()
                ans = max(ans,freq[num][-1] + freq[num][-2])

        return ans