class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = count = 0
        min_len = float('inf')
        n = len(s)
        ans = ""
        for r in range(n):
                if s[r] == '1':
                    count += 1

                while count == k:
                    w = s[l:r+1]
                    if len(w) < min_len or (len(w) == min_len and w < ans):
                        ans = w
                        min_len = min(min_len,r-l+1)
                    if s[l] == '1':
                        count -= 1
                    l += 1
                

        return ans

            