from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        max_countv = 0
        max_countc = 0
        for ch,freq in c.items():
            if ch in "aeiou":
                countv = freq
                max_countv = max(max_countv,countv)
            else:
                countc = freq
                max_countc = max(max_countc,countc)

        return max_countv + max_countc

        