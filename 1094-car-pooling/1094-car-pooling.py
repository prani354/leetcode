import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        heap = []
        for pas,start,end in trips:
            heap.extend([(start,pas),(end,-pas)])
        
        heapq.heapify(heap)
        #print(locations)

        while capacity >= 0 and heap:
            capacity -= heapq.heappop(heap)[1]
        return len(heap) == 0