class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        val = 0

        for bit in nums:
            val = (val * 2 + bit) % 5
            if val % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res

