from typing import List


class Solution:

    def swap(self, nums: List[int], a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        modifications = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:

                if modifications == 1:
                    print(nums)
                    return False

                modifications += 1
                if i - 1 >= 0:
                    if nums[i - 1] > nums[i+1]:
                        nums[i+1] = nums[i]

                    else:
                        nums[i] = nums[i+1]
        
        print(nums)
        if modifications > 1:
            return False
            
      
        return True




result = Solution()
answer = result.checkPossibility([4,2,3])
print("expected answer", True)
print("actual answer", answer)


result = Solution()
answer = result.checkPossibility([4,2,1])
print("expected answer", False)
print("actual answer", answer)

result = Solution()
answer = result.checkPossibility([3,4,2,3])
print("expected answer", False)
print("actual answer", answer)

result = Solution()
answer = result.checkPossibility([5,7,1,8])
print("expected answer", True)
print("actual answer", answer)
