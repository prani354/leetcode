class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = float('-inf')
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    area = 0.5 * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1]))
                    max_area = max(max_area,area)

        return max_area
                    
        