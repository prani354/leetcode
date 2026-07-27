class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        def find(n):

            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1,n2):
            if find(n1) == find(n2):
                return False
            
            r1,r2 = find(n1),find(n2)

            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]

            else:
                parent[r1] = r2
                rank[r2] += rank[r1]

            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
                