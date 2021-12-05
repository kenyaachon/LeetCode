from typing import List


class Solution:
    """
    targetIndex
    go through the list
        if num is equal to target
            targetIndex = num

    if targetIndex == -1
        return [-1, -1]

    start at target index, 
    keep traversing until the num is no longer equal to target
        return [targetIndex, currentIndex-1]


    ex:
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return [0, 0]
        #     return [-1, -1]

        targetIndex = -1
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndex = i
                break

        if targetIndex == -1:
            return [-1, -1]

        for currentIndex in range(targetIndex, len(nums)):
            if nums[currentIndex] != target:
                return [targetIndex, currentIndex - 1]

        return [targetIndex, len(nums) -1]



result = Solution()
answer = result.searchRange([5,7,7,8,8,10], 8)
print("expected result [3, 4]")
print("actual answer:", answer)



answer = result.searchRange([5,7,7,8,8,10], 6)
print("expected result [-1, -1]")
print("actual answer:", answer)


answer = result.searchRange([], 0)
print("expected result [-1, -1]")
print("actual answer:", answer)

answer = result.searchRange([1], 1)
print("expected result [0, 0]")
print("actual answer:", answer)

answer = result.searchRange([1, 1], 1)
print("expected result [0, 1]")
print("actual answer:", answer)

