from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        #check for one size list
        if (len(words) == 1):
            return True

        #sort the letters by weight
        alienDict = {}
        for i in range(len(order)):
            alienDict[order[i]] = i
        

        def lexograph(word: str) -> int:
            wordSize = 0
            for i in word:
                wordSize += alienDict[i]

            return wordSize

        #sort through the numbers
        for i in range(1, len(words)):
            # first, second = words[i], words[i+1]
            first = words[i - 1]
            
            second = words[i]

            #find the min size for comparing
            minSize = min(len(first), len(second))

            firstSize = lexograph(first[:minSize]) 
            secondSize = lexograph(second[:minSize])
            firstLetter = lexograph(first[:1])
            secondLetter = lexograph(second[:1])
            # print(first, second)
                # print(firstSize, secondSize)
            if firstLetter > secondLetter:
                print(firstLetter, secondLetter)
                print(firstSize, secondSize)
                return False
            elif firstSize > secondSize and firstLetter > secondLetter:
                return False

            elif firstSize == secondSize and len(first) > len(second):
                return False

        return True



solution = Solution()
print("Expected result true words : [hello,leetcode], order: hlabcdefgijkmnopqrstuvwxyz")
print("Actual results", solution.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))


print("Expected result false words : [word,world,row], order: [worldabcefghijkmnpqstuvxyz]")
print("Actual results", solution.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))

print("Expected result false words : [apple,app], order: [abcdefghijklmnopqrstuvwxyz]")
print("Actual results", solution.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"
))

print("Expected result True words : [mtkwpj,wlaees] order: [evhadxsqukcogztlnfjpiymbwr]")
print("Actual results", solution.isAlienSorted(["mtkwpj","wlaees"],"evhadxsqukcogztlnfjpiymbwr"))


print("Expected result: False", ["shr","jccni"], "yhfztgrulbkapojcqvseixmdnw")
print("Actual result", solution.isAlienSorted(["shr","jccni"],
"yhfztgrulbkapojcqvseixmdnw"))

    