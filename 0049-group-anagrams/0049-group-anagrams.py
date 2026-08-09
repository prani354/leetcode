
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            text = "".join(sorted(s))
            if text not in d:
                d[text] = []
            
            d[text].append(s) 
        
        res = []
        for ans in d.values():
            res.append(ans)

        return res
