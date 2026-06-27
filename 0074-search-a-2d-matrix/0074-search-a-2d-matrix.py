class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            l , h = 0 , len(mat) - 1

            while l <= h:
                mid = (l + h) // 2

                if mat[mid] == target:
                    return True

                elif mat[mid] > target:
                    h = mid - 1
                
                else:
                    l = mid + 1

        return False
