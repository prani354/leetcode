class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        n = len(nums)

        for i in range(1,n):
            if nums[i-1] + 1 == nums[i]:
                prefix += nums[i]

            else:
                break

        #print(prefix)

        nums_set = set(nums)
        while prefix in nums_set:
            prefix += 1

        return prefix