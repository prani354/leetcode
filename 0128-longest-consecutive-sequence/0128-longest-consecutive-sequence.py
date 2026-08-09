class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        streak = 0

        for num in hashset:
            if num - 1 not in hashset:
                curr = num
                curr_streak = 1

                while curr + 1 in hashset:
                    curr_streak += 1
                    curr += 1

                streak = max(streak,curr_streak)

        return streak
                