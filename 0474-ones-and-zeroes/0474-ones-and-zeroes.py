class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @functools.cache
        def helper(i,zeros,ones):
            if i == len(strs):
                return 0
            newz = strs[i].count("0")
            newo = strs[i].count("1")

            # Two options , Include or exclude the strs
            skip = helper(i+1,zeros,ones)
            include = 0

            if zeros+newz <= m and ones+newo <= n:
                include = 1+ helper(i+1,zeros+newz,ones+newo)

            return max(skip,include)
        return helper(0,0,0)
        