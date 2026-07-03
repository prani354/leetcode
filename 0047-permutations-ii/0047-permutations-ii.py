class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in count:
                if count[num] > 0:
                    curr.append(num)
                    count[num] -= 1
                    backtrack()

                    count[num] += 1
                    curr.pop()

        backtrack()
        return res

                    
                