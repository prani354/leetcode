class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        
        #swapping approach
        for non_zero in range(len(nums)):

            if nums[non_zero] != 0:
                nums[zero] , nums[non_zero] = nums[non_zero] , nums[zero]
                zero += 1

        

