class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}

        for i in range(n):
            res = target - nums[i]
            if res in d:
                return [d[res],i]
            else:
                d[nums[i]] = i
