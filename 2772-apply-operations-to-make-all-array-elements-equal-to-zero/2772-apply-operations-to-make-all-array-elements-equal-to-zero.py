class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        opn = [0] * (n+1)
        curr_sum = 0

        for i in range(n):
            curr_sum += opn[i]
            curr = nums[i] - curr_sum

            if curr < 0:
                return False

            if curr > 0:
                if i + k > n: return False
                opn[i+k] -= curr 

            curr_sum += curr

        return True

