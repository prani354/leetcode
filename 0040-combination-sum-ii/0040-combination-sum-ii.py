class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(curr,idx,target):
            if target == 0:
                res.append(curr[:])
                return

            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue # Avoid duplicates

                if candidates[i] > target: break

                curr.append(candidates[i])
                backtrack(curr,i+1,target-candidates[i])
                curr.pop()

        backtrack([],0,target)
        return res