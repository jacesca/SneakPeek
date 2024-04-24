#!/bin/python3
# You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each
# year of their total age. They will only be able to blow
# out the tallest of the candles. Count how many candles
# are tallest.


def birthdayCakeCandles(candles):
    # Write your code here
    max_candle = max(candles)
    return candles.count(max_candle)


if __name__ == '__main__':
    # Example:
    # Input: 4 4 1 3
    # Output: 2
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
