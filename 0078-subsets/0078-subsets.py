class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr,idx):

            if idx == len(nums):
                res.append(curr[:])
                return

            #dont include
            backtrack(curr,idx+1)

            #include
            curr.append(nums[idx])
            backtrack(curr,idx+1)
            curr.pop()

        backtrack([],0)
        return res
