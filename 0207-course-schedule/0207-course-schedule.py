class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deg = [0] * numCourses
        g = defaultdict(list)

        for u, v in prerequisites:
            g[u].append(v)
        #print(g)

        for u in g:
            for v in g[u]:
                deg[v] += 1
        #print(deg)

        q = deque()

        for i in range(numCourses):
            if deg[i] == 0:
                q.append(i)

        #print(q)
        op = []

        while q:
            n = q.popleft()
            op.append(n)

            for i in g[n]:
                deg[i] -= 1

                if deg[i] == 0:
                    q.append(i)

        #print(deg)

        return True if len(op) == numCourses else False