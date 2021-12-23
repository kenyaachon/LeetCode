from typing import List
import math

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = math.inf
        minPos = 0
        max = 0
        maxPos = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
                minPos = i

        for i in reversed(range(minPos, len(prices))):
            if prices[i] > max:
                max = prices[i]
                maxPos = i

        print("min", min)
        print("max", max)
        return prices[maxPos] - prices[minPos]


        

result = Solution()
print("Expected answer, 5")
print("Actual Answer", result.maxProfit([7,1,5,3,6,4]))

print("Expected answer, 0")
print("Actual Answer", result.maxProfit([7,6,4,3,1]))


print("Expected answer, 5")
print("Actual Answer", result.maxProfit([9, 11, 8, 5, 7, 10]))


print("Expected answer, 2")
print("Actual Answer", result.maxProfit([2, 4, 1]))

