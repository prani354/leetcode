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
        
        # Two pointers
        """ 
            For 0(n) solution, first from the beginning to end 
            if colors[i] != left: dist = max(dist,i)
            right = colors[-1] , if colors[i] != right: dist = max(dist,len(colors) - i - 1)

            From the beginning and from the end , two traversal and results the max_dist 
        """