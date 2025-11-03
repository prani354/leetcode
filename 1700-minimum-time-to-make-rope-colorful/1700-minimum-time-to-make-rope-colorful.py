class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        left = 0

        n = len(colors)
        #two pointers
        for right in range(1,n):
            if colors[left] == colors[right]:
                
                if neededTime[left] < neededTime[right]:
                    time += neededTime[left]
                    left = right
                else:
                    time += neededTime[right]

            else:
                left = right

        return time
        