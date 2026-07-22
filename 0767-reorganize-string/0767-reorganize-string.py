class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        prev = None

        maxheap = [[-cnt,char] for char,cnt in counter.items()]
        #Max heap inbuilt function
        heapq.heapify(maxheap)
        res = ""
        while maxheap or prev:

            if not maxheap and prev:
                return "" #Surely the output will have consecutive same chars

            cnt,char = heapq.heappop(maxheap)
            res += char  # Adding the char
            cnt += 1  # Decrementing count

            if prev:
                heapq.heappush(maxheap,prev)
                prev = None # After adding to heap, prev returns to None
            if cnt != 0:
                prev = [cnt,char]

        return res

        