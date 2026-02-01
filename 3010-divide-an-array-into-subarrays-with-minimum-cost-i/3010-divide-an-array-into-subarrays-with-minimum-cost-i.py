class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]

        rem = nums[1:]
        rem.sort()

        return first + rem[0] + rem[1]