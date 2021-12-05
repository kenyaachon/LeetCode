from ast import Str


class Solution:
    def peek(self, stack: list) -> str:
        if len(stack) >= 1:
            return stack[len(stack) - 1]
        return ""
    
    def isValid(self, s):
        if s == "" or s == " ":
            return True

        #place items in stack
        closingChars = {")":"(", "}":"{", "]":"["}
        stack = []
        stack.append(s[0])
        for char in s[1:]:
            top = self.peek(stack)
            if char in closingChars:
                if closingChars[char] == top:
                    print("%s %s", closingChars[char], top)
                    print("just trying to match everything")
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        #check if stack is empty
        if len(stack) == 0:
            return True
        return False


    #possible solution is to use a stack
    """
    
    So in order for the string to be valid
    So what I am thinkinng is that
    I have a stack
    first I check the to of the stack to see if the element is the opposte
    of the the desired character then,
    then we pop of the item on the stack

    but otherwise I keep putting item on the stack

    if the stack is not empty by the end of the string then return false
    ex1:
    ((()))

    so on the stack
    it would be
    ( -> (( -> and then ((( until I meet ) which then will I pop off an item


    [()]

    (
    """

#Test program
# s = " "
# print("should return False")
# print(Solution().isValid(s))



s = "{}"
print("should return True")
print(Solution().isValid(s))


s = "([)]"
print("should return False")
print(Solution().isValid(s))



s = "{[]}"
print("should return True")
print(Solution().isValid(s))

s = "()[]{}"
print("should return True")
print(Solution().isValid(s))

s = "(])"
print("should return False")
print(Solution().isValid(s))