class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr[:])
                return

            #Include the number nums[i]

            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1) #To add the empty set which means not included nums[i]

        backtrack(0)
        return res
