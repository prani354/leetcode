import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        
        while max_heap:
            if len(max_heap) == 1: return -max_heap[0]

            first = -(heapq.heappop(max_heap))
            second = -(heapq.heappop(max_heap))

            if second <= first:
                if second < first:
                    heapq.heappush(max_heap,-(first-second))
                else:
                    heapq.heappush(max_heap,0)

        
        