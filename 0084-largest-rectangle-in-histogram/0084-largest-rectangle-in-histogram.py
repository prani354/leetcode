class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i,height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                j , h = stack.pop()
                w = i - j
                area = h * w
                max_area = max(max_area,area)
                start = j

            stack.append((start,height))

        while stack:
            j , h = stack.pop()
            w = n - j
            area = h * w
            max_area = max(max_area,area)

        return max_area