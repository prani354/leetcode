from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(n):

            hashmap[s[right]] = hashmap.get(s[right],0) + 1

            while hashmap[s[right]] > 2:
                hashmap[s[left]] -= 1
                left += 1

            max_len = max(max_len,right - left + 1)

        return max_len