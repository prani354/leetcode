class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []

        res = []
        n = len(p)

        target = [0] * 26
        window = [0] * 26

        for c in p:
            target[ord(c) - 97] += 1

        for i in range(len(s)):
            window[ord(s[i]) - 97] += 1

            if i >= n:
                window[ord(s[i - n]) - 97] -= 1

            if window == target:
                res.append(i - n + 1)

        return res
