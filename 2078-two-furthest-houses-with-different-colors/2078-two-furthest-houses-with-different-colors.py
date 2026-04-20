class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_len = 0
        length = 0
        for i in range(n):
            for j in range(i+1,n):

                if colors[i] != colors[j]:
                    length = j - i

                max_len = max(max_len,length)

        return max_len
        