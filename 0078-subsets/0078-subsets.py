class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i,ans):
            if i > len(nums):
                return
            
            res.append(ans[:])

            for j in range(i,len(nums)):
                ans.append(nums[j])
                backtrack(j+1,ans)
                ans.pop()

        res =[]
        backtrack(0,[])
        return res
        