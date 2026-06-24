class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_run = [0] * n
        right_run = [0] * n
        l = r = 1

        for i in range(len(nums)):
            left_run[i] = l
            j = - i - 1
            right_run[j] = r
            l *= nums[i]
            r *= nums[j]

        return [l*r for l,r in zip(left_run,right_run)]
            