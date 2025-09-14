class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        
        exact = set(wordlist)
        casemap = {}
        vowelmap = {}

        for w in wordlist:
            lower = w.lower()
            dev = self.devowel(lower)
            if lower not in casemap:
                casemap[lower] = w
            if dev not in vowelmap:
                vowelmap[dev] = w

        res = []

        for q in queries:
            if q in exact:
                res.append(q)
            else:
                lower = q.lower()
                dev = self.devowel(lower)
                if lower in casemap:
                    res.append(casemap[lower])
                elif dev in vowelmap:
                    res.append(vowelmap[dev])
                else:
                    res.append("")
        return res

    def devowel(self,s):
        return "".join('*' if c in "aeiou" else c for c in s)
        