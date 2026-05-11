class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_left = [0]*n
        sum_right = [0]*n

        for i in range(n):
            sum_left[i] = sum(nums[:i])
            sum_right[i] = sum(nums[i+1:])

            if sum_left[i] == sum_right[i]:
                return i

        return -1