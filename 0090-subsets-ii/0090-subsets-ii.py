class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i,ans):
            if i == len(nums):  #Base case
                res.append(ans[:])
                return

            ans.append(nums[i])  #include duplicates in left half
            backtrack(i+1,ans)

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            ans.pop()  #Exclude duplicates
            backtrack(i+1,ans)

        backtrack(0,[])
        return res

