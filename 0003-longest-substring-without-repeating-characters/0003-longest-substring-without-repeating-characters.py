class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = float('-inf')

        if s == "":
            return 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.discard(s[l])
                l += 1

            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len,r-l+1)

            

        return max_len


            
        
            

        