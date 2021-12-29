from math import inf
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        sums = {}
        sums[0] = (nums[0])
        maxNum = -inf
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]
            maxNum = max(maxNum, sums[i])
        
        for i in reversed(range(n)):
            for j in range(i):
                maxNum = max(maxNum, sums[i] - sums[j])
        
        return maxNum


answer = Solution()
print("Expected result, 6")
print("Actual result, ", answer.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


print("Expected result, 23")
print("Actual result, ", answer.maxSubArray([5,4,-1,7,8]))
