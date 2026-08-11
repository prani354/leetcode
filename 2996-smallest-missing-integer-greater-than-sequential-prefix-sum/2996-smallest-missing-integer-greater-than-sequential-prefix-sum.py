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

        if prefix in nums:
            while True:
                if prefix+1 not in nums:
                    return prefix+1
                else:
                    prefix += 1
        
        return prefix