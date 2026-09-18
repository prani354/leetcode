class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        #print(d)
        for ch,count in d.items():
            if count == 1:
                return s.index(ch)

        return -1