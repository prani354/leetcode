class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(1,n):
            sum1 = sum(nums[:i])
            sum2 = sum(nums[i:])

            if abs(sum1 - sum2) % 2 == 0:
                count += 1

        return count
        