class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [(interval[0],i) for i,interval in enumerate(intervals)]
        start.sort()
        print(start)
        res = []

        for interval in intervals:
            end = interval[1]
            idx = -1
            left,right = 0,len(start)-1

            while left <= right:
                mid = (left + right) // 2

                if start[mid][0] >= end:
                    idx = start[mid][1]
                    right = mid - 1

                else:
                    left = mid + 1

            res.append(idx)
        return res
                