import heapq
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        online = [True] * (c+1)
        adj = defaultdict(list)

        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        sub = []
        station = {}

        def get_network(node,st):
            if node in station:
                return 

            station[node] = st
            heapq.heappush(sub[st],node)
            for ch in adj[node]:
                get_network(ch,st)

        curr = -1

        for node in range(1,c+1):
            if node not in station:
                curr += 1
                sub.append([])
            get_network(node,curr)

        ans = []

        for q,node in queries:
            station_id = station[node]
            st = sub[station_id]

            if q == 2:
                online[node] = False
                while st and not online[st[0]]:
                    heapq.heappop(st)

            else:
                if online[node]:
                    ans.append(node)
                    continue
                nearest = -1
                if st:
                    nearest = st[0]
                ans.append(nearest)

        return ans
        