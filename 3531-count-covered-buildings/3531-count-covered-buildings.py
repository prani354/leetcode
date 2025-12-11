class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        dict_x = {}
        dict_y = {}

        for b in buildings:
            if b[0] not in dict_x:
                dict_x[b[0]] = SortedList([b[1]])
            else:
                dict_x[b[0]].add(b[1])

            if b[1] not in dict_y:
                dict_y[b[1]] = SortedList([b[0]])
            else:
                dict_y[b[1]].add(b[0])

        res = 0
        for b in buildings:
            x = b[0]
            y = b[1]

            if dict_x[x][0] != y and dict_x[x][-1] != y and dict_y[y][0] != x and dict_y[y][-1] != x:
                res += 1

        return res