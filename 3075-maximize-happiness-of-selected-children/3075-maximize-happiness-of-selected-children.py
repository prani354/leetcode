class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        i = 0
        res = 0

        while k > 0 and happiness[i] -  i > 0:
            res += happiness[i] - i
            k -= 1
            i += 1

        return res