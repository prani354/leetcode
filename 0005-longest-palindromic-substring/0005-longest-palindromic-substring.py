class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        # Expanding from the center potential at each indices

        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            
            odd = expand(i,i)
            even = expand(i,i+1)

            if len(longest) < len(odd):
                longest = odd
            if len(longest) < len(even):
                longest = even

        return longest

