class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0

        for r in bank:
            curr = r.count('1')

            if curr > 0:
                ans += prev * curr
                prev = curr

        return ans