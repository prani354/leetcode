class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(1,n+2):
            if (i * k) not in nums:
                return i * k
