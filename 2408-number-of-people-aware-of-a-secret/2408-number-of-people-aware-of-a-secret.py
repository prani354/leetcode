class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        secret = [0] * n
        spread = 0
        res = 1

        secret[0] = 1

        for day in range(1,n):
            if day >= delay:
                spread += secret[day - delay]
            if day >= forget:
                forgot = secret[day - forget]
                res -= forgot
                spread -= forgot

            secret[day] = spread
            res += spread

        return res % (10 ** 9 + 7)
        