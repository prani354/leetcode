import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = Counter(nums)

        for key, value in freq.items():
            heapq.heappush(heap,(value,key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for key,value in heap:
            res.append(value)

        return res

        

        