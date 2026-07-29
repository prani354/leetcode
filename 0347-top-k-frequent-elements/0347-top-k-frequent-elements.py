import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = Counter(nums)
        res = 0

        for key,value in freq.items():
            heapq.heappush(heap,(value,key))

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        res = []
        for v,k in heap:
            res.append(k)

        return res

        

        