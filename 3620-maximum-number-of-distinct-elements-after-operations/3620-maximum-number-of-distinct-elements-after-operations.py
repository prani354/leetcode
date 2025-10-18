class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        l_p = -10 ** 10

        count = 0

        for num in nums:
            l_bound = num - k
            u_bound = num + k

            if l_p < l_bound:
                l_p = l_bound
            else:
                l_p += 1

            if l_p <= u_bound:
                count += 1
            else:
                l_p -= 1

        return count
