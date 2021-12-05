from typing import List


class Solution:
    """
    Easy way to do it would be to have a 2 for loops traverse the list
    once you have two items that equal the target
    return the two items in a list
    otherwise return [-1, -1]

    what would be a faster solution
    if the number is smaller than the target then add it to the working set

    then go through the set and solve the number
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # workingSet = []
        # for num in nums:
        #     if num < target:
        #         workingSet.append(num)

        # for i in range(len(workingSet)):
        #     for j in range(i, len(workingSet)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        workingSet = []
        for i in range(len(nums)):
            if nums[i] <= target:
                workingSet.append([ nums[i], i])


        for i in range(len(workingSet)):
            for j in range(i + 1, len(workingSet)):
                # if nums[i] + nums[j] == target:
                if workingSet[i][0] + workingSet[j][0] == target:
                    return [workingSet[i][1], workingSet[j][1]]





result = Solution()


answer = result.twoSum([2,7,11,15], 9)
print("expected answer [0,1]")
print("Actual answer", answer)


answer = result.twoSum([3,2,4], 6)
print("expected answer [1,2]")
print("Actual answer", answer)

answer = result.twoSum([3,3], 6)
print("expected answer [0,1]")
print("Actual answer", answer)

answer = result.twoSum([2,5, 5, 11], 10)
print("expected answer [1,2]")
print("Actual answer", answer)

answer = result.twoSum([0,4,3,0]
, 0)
print("expected answer [0,3]")
print("Actual answer", answer)
