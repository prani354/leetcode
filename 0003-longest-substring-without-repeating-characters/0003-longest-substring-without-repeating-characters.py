class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):

            while s[right] in st:
                st.remove(s[left])
                left += 1

            st.add(s[right])
            curr_length = right - left + 1
            max_length = max(max_length , curr_length)

        return max_length