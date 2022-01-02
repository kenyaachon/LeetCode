from math import inf
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        subArray = maxSubArray = nums[0]
        #kaddian algorithm
        #time complexity O(n)
        #space complexity O(1)
        for i in range(1, len(nums)):
            subArray = max(nums[i], subArray + nums[i])

            maxSubArray = max(subArray, maxSubArray)

        return maxSubArray


answer = Solution()
print("Expected result, 6")
print("Actual result, ", answer.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


print("Expected result, 23")
print("Actual result, ", answer.maxSubArray([5,4,-1,7,8]))


print("Expected result, -1")
print("Actual result, ", answer.maxSubArray([-1, -2]))

