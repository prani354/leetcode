class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        max_sum = 0
        left = 0
        curr_sum = 0
        wind = set()

        for right in range(len(nums)):

            while nums[right] in wind or right - left + 1 > k:
                wind.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            wind.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum,curr_sum)

        return max_sum



        


        