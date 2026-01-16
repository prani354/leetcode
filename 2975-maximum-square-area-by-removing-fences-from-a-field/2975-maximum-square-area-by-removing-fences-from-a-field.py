class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def solve(arr):
            x = set()
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    x.add(arr[j]-arr[i])

            return x

        MOD = 10 ** 9 + 7
        h_fences = [1] + hFences + [m]
        v_fences = [1] + vFences + [n]
        h_fences.sort()
        v_fences.sort()

        h = solve(h_fences)
        v = solve(v_fences)
        max_area = -1

        for i in list(h):
            if i in v:
                max_area = max(max_area,i)

        return (max_area ** 2) % MOD if max_area != -1 else -1