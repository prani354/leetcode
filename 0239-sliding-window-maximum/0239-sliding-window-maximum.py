from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()

        if not nums:
            return []

        if k == 1:
            return nums

        for i in range(len(nums)):
            #validity range

            while q and q[0] < i-k+1:
                q.popleft()
            
            #popping out the minimum value
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            #appending the maximum value from each window
            if i >= k-1:
                output.append(nums[q[0]])

        return output

            

        