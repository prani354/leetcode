class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if k == 0:
            return

        count = 0
        st = 0

        while count < n:
            curr_idx = st
            in_hand = nums[st]

            while True:
                next_idx = (curr_idx + k) % n
                nums[next_idx] , in_hand = in_hand , nums[next_idx]
                curr_idx = next_idx
                count += 1

                if curr_idx == st:
                    break

            st += 1
            
        
        