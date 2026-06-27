class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def speed(mid):
            tot = 0
            for i in range(len(dist)-1):
                tot += math.ceil(dist[i]/mid)

            tot += dist[-1] / mid

            return tot

        l = 1
        h = 10**7
        res = -1

        while l <= h:
            mid = (l + h) // 2

            if speed(mid) <= hour:
                res = mid
                h = mid - 1
            else:
                l = mid + 1

        return res
