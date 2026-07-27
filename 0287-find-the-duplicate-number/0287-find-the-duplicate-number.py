class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [0] * (len(nums)+1)

        for i in range(len(nums)):
            freq[nums[i]] += 1

        print(freq)

        for i in range(len(freq)):
            if freq[i] > 1:
                return i

