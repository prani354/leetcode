from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # q = deque(nums[:k])  It is a TLE solution but this also correct solution

        # res = []
        # res.append(max(q))
        # #print(res)
        # r = len(q)
        # while r < n:
        #     q.popleft()
        #     q.append(nums[r])
        #     res.append(max(q))
        #     r += 1

        # return res

        # Optimized solution
        q = deque()
        n = len(nums)
        res = []

        if not nums: return []
        if k == 1: return nums

        for i in range(n):
            while q and q[0] < i-k+1:
                q.popleft() # Validating the k-range
            
            while q and nums[q[-1]] < nums[i]: # Stack like to remove minimum value
                q.pop()

            q.append(i) #Idx queue

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
