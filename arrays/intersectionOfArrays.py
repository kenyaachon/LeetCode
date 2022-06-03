"""

given 2 arrays
return an array of their intersection

each elementin the result must be unique and you may return the result in any order

[1,2,2,1] 
[2, 2]

[2]

[4,9,5]

[9,4,9,8,4]

[4, 9, 5]

make a set of the bigger list

go through the other list
    if the current item is in the set
        add to the results set

convert the results set to an array
return results

time complexity O(n)
space complexity O(n)

example

[9,4,9,8,4] < set

[4, 9, 5]

i = 0
4 is in the set

[4]
i= 1
9 is in the set
[4, 9]

i = 2
5 is in the set

return 






"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #make set of the bigger list
        store = set(nums1)
        
        
        result = set()
        for i in range(len(nums2)):
            if nums2[i] in store:
                result.add(nums2[i])

        return list(result)



solution = Solution()
print(solution.intersection([9,4,9,8,4] ,[4, 9, 5]))
print("expected [4, 9, 5]")

print(solution.intersection([1,2,2,1] ,[2,2]))
print("expected [2]")