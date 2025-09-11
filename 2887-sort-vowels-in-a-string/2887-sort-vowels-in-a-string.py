class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = []
        s = list(s)
        for c in s:
            if c in "AEIOUaeiou":
                vowel.append(c)
            
        vowel.sort()
        j = 0
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i] = vowel[j]
                j += 1

        return "".join(s)
        