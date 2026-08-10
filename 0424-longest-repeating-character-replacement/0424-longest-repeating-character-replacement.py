class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        max_count = 0
        max_length = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right],0) + 1
            max_count = max(max_count,hashmap[s[right]])

            if (right - left + 1 - max_count) > k:
                hashmap[s[left]] -= 1
                left += 1

            max_length = max(max_length,right-left+1)

        return max_length
