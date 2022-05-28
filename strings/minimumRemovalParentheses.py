"""
Given a string of parentheses

your task is to remove the minimum number of parentheses
so that the result parenthese string is valid

and return any valid string

Ok so do I count the number of strings and remove them from the string

input: lee(t(c)o)de)

output: lee(t(c)o)de)

stack:


) -> what is the position of this parentheses
then remove the parenthese from the string

return the string

input: a)b(c)d
output: ab(c)d

) -> what is the position of this parenthese
ok so in the stack, I need to store the character and the position it was at


possible way:
traverse the string
    if the character is a closing parenthese
        check the top of the stack, if it an opening parenthese
            then pop off the stack
    else:
        add the parenthese to the stack and its position

traverse the stack until it is empty
    pop of the top item 
    remove the top item from the original string

return the desired string

input:
))((
ouput:


stack

# (, 3
# (, 2
# ), 1
# ), 0

go through the stack:
original string

ouput: 

time complexity
O(n) + O(nlogn) -> O(nlogn)
Space complexity


"""

import time


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        copy = list(s)

        #traverse the string
        for i in range(len(copy)):
            if len(stack):
                if copy[i] == ')' and stack[-1][0] == '(':
                    stack.pop()
                elif copy[i] == ')' or copy[i] == '(':
                    stack.append([copy[i], i])
            elif copy[i] == ')' or copy[i] == '(':
                stack.append([copy[i], i])

        print(stack)
        # traverse the stack
        while len(stack):
            item = stack.pop()
            copy.pop(item[1])
        
        result = ''
        for sub in copy:
            result += sub

        return result





solution = Solution()
start = time.time()
print ("expected result lee(t(c)o)de")
print ("actual character ", solution.minRemoveToMakeValid("lee(t(c)o)de)"))
end = time.time()
print("actual time", end - start)

solution = Solution()
start = time.time()
print ("expected result ab(c)d")
print ("actual character ", solution.minRemoveToMakeValid( "a)b(c)d"))
end = time.time()
print("actual time", end - start)

solution = Solution()
print ("expected result ")
print ("actual character ", solution.minRemoveToMakeValid( "))(("))

