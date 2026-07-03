class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []

        res = []
        candidates.sort()

        def backtrack(start,curr,total):
            if total > target:
                return

            if total == target:
                res.append(curr)
                return 

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                backtrack(i+1,curr+[candidates[i]], total + candidates[i])

        backtrack(0,[],0)

        return res