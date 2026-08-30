class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # if n == 2:
        #     return n

        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))

        # #print(max_idx,min_idx)

        # remove_max = min((max_idx-0),(n-max_idx))
        # remove_min = min((min_idx-0),(n-min_idx))

        # if max_idx + 1 == min_idx or min_idx + 1 == max_idx:
        #     return remove_max + remove_min

        # return remove_max + remove_min + 1

        left = min(min_idx,max_idx)
        right = max(min_idx,max_idx)

        front = right + 1
        back = n - left
        front_back = left + 1 + n - right

        return min(front,back,front_back)
        