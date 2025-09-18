class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            min_val = min(min_val,nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid-1

        return min_val
        