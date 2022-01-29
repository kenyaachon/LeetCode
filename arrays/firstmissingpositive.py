from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            table[num] = num

        for i in range(len(nums)+1):
            if i + 1 not in table:
                return i + 1
        return 1


answer = Solution()

print("Expected answer 3")
print("Actual Answer", answer.firstMissingPositive([1,2,0]))

print("Expected answer 2")
print("Actual Answer", answer.firstMissingPositive([3,4,-1,1]))

print("Expected answer 1")
print("Actual Answer", answer.firstMissingPositive([7,8,9,11,12]
))


print("Expected answer 2")
print("Actual Answer", answer.firstMissingPositive([1]
))



