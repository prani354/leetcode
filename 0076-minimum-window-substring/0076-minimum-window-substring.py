class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(t)
        n = len(s)

        count = 0
        hashmap = [0] * 256
        min_len = 10 ** 9
        st_idx = -1   
        l = r = 0
        
        for i in range(m):
            hashmap[ord(t[i])] += 1

        while r < n:
            if hashmap[ord(s[r])] > 0:
                count += 1
            hashmap[ord(s[r])] -= 1
            r += 1

            while count == m:
                if r - l < min_len:
                    min_len = r - l
                    st_idx = l

                
                hashmap[ord(s[l])] += 1
                if hashmap[ord(s[l])] > 0:
                    count -= 1
                l += 1

        return "" if st_idx == -1 else s[st_idx:st_idx + min_len]
