class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        def prefix(string):
            if len(s) < len(string):
                return False

            return s.startswith(string)
        
        count = 0
        for string in words:
            if prefix(string):
                count += 1

        return count
        

        
