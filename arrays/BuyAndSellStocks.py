from typing import List
import math

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        profit = 0
        biggestNum = prices[len(prices) - 1]
        for i in reversed(range(len(prices))):
            profit = max(profit, biggestNum - prices[i])
            biggestNum = max(biggestNum, prices[i])

        return profit
        

result = Solution()
print("Expected answer, 5")
print("Actual Answer", result.maxProfit([7,1,5,3,6,4]))

print("Expected answer, 0")
print("Actual Answer", result.maxProfit([7,6,4,3,1]))


print("Expected answer, 5")
print("Actual Answer", result.maxProfit([9, 11, 8, 5, 7, 10]))


print("Expected answer, 2")
print("Actual Answer", result.maxProfit([2, 4, 1]))

print("Expected Answer, 4")
print("Actual Answer", result.maxProfit([3,2,6,5,0,3]))


