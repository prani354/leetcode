class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles

        while numBottles >= numExchange:
            value = numBottles // numExchange
            drank += value

            numBottles %= numExchange
            numBottles += value

        return drank
