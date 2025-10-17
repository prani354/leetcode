class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def dfs(i, mask, changed):
            if i == n:
                if changed:
                    return 1
                return -inf

            a = s[i]
            od = ord(a) - ord('a')
            res = 0
            newmask = mask | (1 << od)
            if k < format(newmask, 'b').count('1'):
                res = max(dfs(i + 1, 1 << od, changed) + 1, res)
            else:
                res = max(dfs(i + 1, newmask, changed), res)
            if changed:
                return res
            for q in range(26):
                if q == od:
                    continue
                newmask = mask | (1 << q)
                if k < format(newmask, 'b').count('1'):
                    res = max(dfs(i + 1, 1 << q, True) + 1, res)
                else:
                    res = max(dfs(i + 1, newmask, True), res)
            return res
        return dfs(0, 0, False)