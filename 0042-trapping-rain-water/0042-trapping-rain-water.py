class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right =[0] * n
        left = [0] * n
        res = 0

        left[0] = height[0]
        right[n-1] = height[n-1]

        for i in range(1,n):
            j = -i-1
            left[i] = max(left[i-1],height[i])
            right[j] = max(right[j+1],height[j])
        
        for i in range(1,n-1):
            left_max = left[i]
            right_max = right[i]

            if height[i] < left_max and height[i] < right_max:
                res += min(left_max,right_max) - height[i]

        return res
        
