from typing import List
import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        time complexity = O(nlogn)
        space complexity = O(n)
        """
        numsList = sorted(nums)
        
        n = len(numsList)
        return max(numsList[n-1] * numsList[n-2] * numsList[n-3], numsList[0] * numsList[1] * numsList[n-1])


answer = Solution()
# print("Expected answer, 6")
# print("Actual answer, ", answer.maximumProduct([1,2,3]))

# print("Expected answer, 24")
# print("Actual answer, ", answer.maximumProduct([1,2,3, 4]))

# print("Expected answer, -6")
# print("Actual answer, ", answer.maximumProduct([-1, -2, -3]))

# print("Expected answer, 39200")
# print("Actual answer, ", answer.maximumProduct([-100,-98,-1,2,3,4]))

print("Expected answer, 300")
print("Actual answer, ", answer.maximumProduct([-100, -2, -3, 1]))