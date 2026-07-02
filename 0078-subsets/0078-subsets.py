class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):

            if i >= len(nums):
                res.append(curr[:])
                return

            #Include the number
            curr.append(nums[i])
            dfs(i+1)

            #Not include the number
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res