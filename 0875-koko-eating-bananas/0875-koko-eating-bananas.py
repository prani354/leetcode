class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2

            tot = 0
            for pile in piles:
                tot += math.ceil(pile/mid)

            if tot <= h:
                res = mid
                r = mid - 1

            else:
                l = mid + 1

        return res