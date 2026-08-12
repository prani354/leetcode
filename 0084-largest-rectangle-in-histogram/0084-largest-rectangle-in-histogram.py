class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for idx,height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i,h = stack.pop()
                max_area = max(max_area,h*(idx-i))
                start = i

            stack.append((start,height))

        for i,h in stack:
            max_area = max(max_area,h*(n-i))

        return max_area