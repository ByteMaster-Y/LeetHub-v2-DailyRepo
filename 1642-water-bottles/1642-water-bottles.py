class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        plus_bottle = numBottles // numExchange
        rest_bottle = numBottles % numExchange
        current = plus_bottle
        while current > 0:
            current, rem = divmod(current + rest_bottle, numExchange)
            plus_bottle += current
            rest_bottle = rem
        return plus_bottle + numBottles