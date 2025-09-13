class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_store = 0
        i = 0
        j = len(height) - 1

        while i < j:
            max_store = max(max_store,min(height[i],height[j])*(j-i))

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_store
        