class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(num for num in nums if num % 2 == 0)

        if not counter:
            return -1

        m = max(counter.values())
        res = min(x for x,v in counter.items() if v == m)
        return res
