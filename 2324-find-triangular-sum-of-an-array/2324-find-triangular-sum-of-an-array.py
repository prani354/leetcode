class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            res = []

            for i in range(1,len(nums)):
                res.append((nums[i-1]+nums[i]) %  10)

            nums = res

        return nums[0]
             