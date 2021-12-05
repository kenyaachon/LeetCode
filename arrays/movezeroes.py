from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Go through the array
        if a number is not zero, 
            append the number to nonzero list
        
        Go through the array
            if number is zero, append to array

        for elements in list
            oldlistitem = list[i]

        ex:
        0,1,0,3, 12

        0, 0,       1,3,12



        """
        if len(nums) == 1:
            return

        temp = []
        for num in nums:
            if num != 0:
                temp.append(num)

        for num in nums:
            if num == 0:
                temp.append(num)

        for i in range(len(nums)):
            nums[i] =  temp[i]

        

input = [0,1,0,3,12]
result = Solution()
result.moveZeroes(input)
print("expected answer", [1,3,12,0,0])
print("actual answer", input)