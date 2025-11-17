class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = []

        for i,num in enumerate(nums):
            if num == 1:
                res.append((i,num))
        
        print(res)

        for i in range(1,len(res)):
            if (res[i][0] - res[i-1][0])-1 < k:
                return False

        return True