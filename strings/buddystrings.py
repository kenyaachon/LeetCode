class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        changes = 0
        swapChars = []
        repeat = {}
        repeats = 0
        for i in range(len(goal)):
            if s[i] in repeat:
                repeats += 1
            else:
                repeat[s[i]] = s[i]

            if goal[i] != s[i]:
                changes += 1
                swapChars.append([i, s[i]])


        if changes < 2 or changes > 2:
            if changes < 1 and repeats >= 1:
                return True

            return False
        else:
            tempstring = list(s)
            first = swapChars[0]
            second = swapChars[1]
            tempstring[first[0]] = second[1]
            tempstring[second[0]] = first[1]
            if ''.join(tempstring) == goal:
                return True
            return False
        


print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))

print (Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))


print (Solution().buddyStrings('aa', 'aa'))

print (Solution().buddyStrings('ab', 'ab'))