class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_len = 0
        left = colors[0]

        for i in range(1,n):
            if colors[i] != left:
                max_len = max(max_len,i)
        
        right = colors[-1]

        for i in range(n-1,-1,-1):
            if colors[i] != right:
                max_len = max(max_len, n-i-1)

        return max_len

        
        # Two pointers
        """ 
            For 0(n) solution, first from the beginning to end 
            if colors[i] != left: dist = max(dist,i)
            right = colors[-1] , if colors[i] != right: dist = max(dist,len(colors) - i - 1)

            From the beginning and from the end , two traversal and results the max_dist 
        """