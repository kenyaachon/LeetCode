from typing import List
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength = math.inf

        maxSum = 0
        for i in range(len(nums)):
            maxSum += nums[i]
        if maxSum < target:
            return 0

        for i in range(len(nums)):
            sum = 0
            length = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                length += 1
                if sum >= target:
                    if minlength >= length:
                        minlength = length
                        break
        if minlength == math.inf:
            return 0
        else: 
            return minlength



answer = Solution()

print("Expected result 2")
print("Actual result", answer.minSubArrayLen(7, [2,3,1,2,4,3]))

print("Expected result 1")
print("Actual result", answer.minSubArrayLen(4, [1, 4, 4]))
print("Expected result 0")
print("Actual result", answer.minSubArrayLen(11, [1,1,1,1,1,1,1,1]
))
