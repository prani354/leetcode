from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        
        for key,val in counter.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [key for(val,key) in heap]

        
        




        
        