class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        end = max(nums)
        res = []

        for i in range(start,end+1):
            if i not in nums:
                res.append(i)

        return res


