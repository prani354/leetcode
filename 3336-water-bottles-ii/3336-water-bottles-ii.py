class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty = 0

        while True:
            if numBottles > 0:
                drank += numBottles
                empty += numBottles
                numBottles = 0

            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1

            if numBottles == 0:
                return drank