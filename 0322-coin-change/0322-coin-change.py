from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append([0,0])
        visited = set()

        while q:
            curr,level = q.popleft()
            if curr == amount:
                return level

            for coin in coins:
                c = coin+curr
                if c <= amount and c not in visited:
                    q.append([c,level+1])
                    visited.add(c)

        return -1
        
        