from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        time = 0
        q = deque()

        while q or heap:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append([cnt,time+n])

            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])

        return time
                

        