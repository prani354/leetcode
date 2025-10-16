class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem_count = [0] * value

        for num in nums:
            rem = ((num % value) + value) % value
            rem_count[rem] += 1

        res = 0 
        while rem_count[res % value] > 0:
            rem_count[res % value] -= 1
            res += 1

        return res