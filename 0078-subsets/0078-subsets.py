class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr,idx):

            if idx == len(nums):
                res.append(curr[:])
                return

            #include
            curr.append(nums[idx])
            backtrack(curr,idx+1)

            #not include
            curr.pop()
            backtrack(curr,idx+1)

        backtrack([],0)
        return res
