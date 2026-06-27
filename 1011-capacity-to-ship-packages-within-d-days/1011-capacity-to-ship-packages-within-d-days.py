class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)

        def helper(mid,weights):

            count = 1
            curr_sum = 0

            for weight in weights:
                if curr_sum + weight > mid:
                    curr_sum = weight
                    count += 1

                else:
                    curr_sum += weight

            return count

        while l < h:
            mid = l + (h-l) // 2

            if helper(mid,weights) <= days:
                h = mid 

            else:
                l = mid + 1

        return l
        