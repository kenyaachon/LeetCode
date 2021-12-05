from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        so for sure if the array is size 1 do nothing

        traverse the array
        for each color when we a find a a new one, increment the count for that color

        for each key, value pair in the dict
            append the key to the list up to the limit of the value

        set nums to temp 


        2 0 2 1 1 0

        0: 2, 1: 2, 2: 2

        0, 0, 1, 1, 2, 2


        """       
        if len(nums) == 1:
            return

        colors = {0:0, 1: 0, 2: 0}
        for num in nums:
            colors[num] = colors[num] + 1

        for key, value in colors.items():
            for j in range(value):
                nums.append(key)        
                nums.pop(0)
        print("actual numbers", nums)


result = Solution()
answer = result.sortColors([2,0,2,1,1,0])
print("expected answer [0,0,1,1,2,2]")

answer = result.sortColors([2,0,1])
print("expected answer [0,1,2]")

answer = result.sortColors([2,0,1])
print("expected answer [0,1,2]")

answer = result.sortColors([0])
print("expected answer [0]")

answer = result.sortColors([1])
print("expected answer [1]")

