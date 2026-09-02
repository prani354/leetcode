class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        count = 0
        last = 0

        for i in range(len(nums)-1):
            far = max(far,i+nums[i])

            if i == last:
                last = far
                count += 1

        return count
