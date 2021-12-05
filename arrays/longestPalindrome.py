class Solution:
    """
    store a variable named largestPalindrome

    traverse through the string
    add new characters to the string
    check if it is a palindrome
        check if the len of the temp > largestPalindrome
            set largestPalindrome = temp

    resetTemp

    return largestPalindrome



    ex: babad
    b < largestPalindrome
    ba
    bab < largestPalindrome
    baba
    babad

    a < largestPalindrome
    ac 


    c
    cb
    cbb
    cbbd
    b
    bb

    
    """

    def checkPalindrome(self, s:str) -> bool:
        if s == s[::-1]:
            return True
        return False

    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        longestPalindrome = ""
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp = temp + s[j]
                if temp == temp[::-1]:
                    if len(temp) > len(longestPalindrome):
                        longestPalindrome = temp

            if (len(s) - i) < len(longestPalindrome):
                return longestPalindrome

        return longestPalindrome
                


        


result = Solution()
answer = result.longestPalindrome("babad")
print("expected string: bab")
print("actual string: ", answer)


answer = result.longestPalindrome("cbbd")
print("expected string: bb")
print("actual string: ", answer)


answer = result.longestPalindrome("ac")
print("expected string: a")
print("actual string: ", answer)

answer = result.longestPalindrome("a")
print("expected string: a")
print("actual string: ", answer)

