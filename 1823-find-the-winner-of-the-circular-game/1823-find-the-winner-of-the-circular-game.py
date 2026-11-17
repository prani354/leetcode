class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        person = 1

        for i in range(1,n):
            person = (person + k - 1) % (i+1) + 1

        return person