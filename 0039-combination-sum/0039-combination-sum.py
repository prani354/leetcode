class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr,idx,remsum):
            if remsum == 0:
                res.append(curr[:])
                return

            if remsum < 0 or idx >= len(candidates):
                return

            curr.append(candidates[idx])
            backtrack(curr,idx,remsum - candidates[idx])
            curr.pop()
            backtrack(curr,idx+1,remsum)

        backtrack([],0,target)
        return res
