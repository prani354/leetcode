import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r)//2
            total = 0

            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)

            if total <= h:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans
