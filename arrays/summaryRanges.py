from typing import List

"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

"""

class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]

        ranges = []
        first = nums[0]
        last = nums[0]

        
        #traverse the list
        for i in range(1, n):
            
            #check if current item is a continuation
            if nums[i] == last or nums[i] == last+1:
                last = nums[i]

            #check whether the range is only one item
            else:
                if last == first:
                    ranges.append(str(last))
                else:
                    comp = str(first) + "->" + str(last)
                    ranges.append(comp)

                first = nums[i]
                last = nums[i]

        #last range
        if last == first:
            ranges.append(str(last))
        else:
            comp = str(first) + "->" + str(last)
            ranges.append(comp)

        return ranges


solution = Solution()
print('Expected "0->2","4->5","7"}')
print(solution.summaryRanges([0,1,2,4,5,7]))

print('Expected ["0","2->4","6","8->9"]')
print(solution.summaryRanges([0,2,3,4,6,8,9]))