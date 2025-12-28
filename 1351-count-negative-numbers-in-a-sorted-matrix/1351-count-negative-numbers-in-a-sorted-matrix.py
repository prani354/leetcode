class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for mat in grid:
            for num in  mat:
                if num < 0:
                    count += 1

        return count
        
        # def binary_search(mat):
        #     l = 0
        #     r = len(mat) - 1
        #     count = 0
        #     while l <= r:
        #         m = (l+r) // 2

        #         if mat[m] < 0:
        #             count += (len(mat) - m)
        #             return count
                
        #         elif mat[m] >= 0:
        #             l = m + 1
        # res = 0
        # for mat in grid:
        #     res += binary_search(mat)

        # return res



        