import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = Counter(nums)

        for key,value in d.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
            
            
        print(heap)

        return [num for freq,num in heap]
        
        

        