from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [[strs[0]]]
        anagrams = {}
        for subStr in strs:
            stVal = str(sorted(subStr))
            
            if stVal in anagrams:
                anagrams[stVal].append(subStr)
            else:
                anagrams[stVal] = [subStr]
        return list(anagrams.values())

solution = Solution()
print('expect answer [["bat"],["nat","tan"],["ate","eat","tea"]] ')
print(f'actual answer {solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])}')

solution = Solution()
print('expect answer [['']]')
print(f'actual answer {solution.groupAnagrams([""])}')

solution = Solution()
print("expect answer [['a']]")
print(f'actual answer {solution.groupAnagrams(["a"])}')

solution = Solution()
print("expect answer [['a']]")
print(f'actual answer {solution.groupAnagrams(["a"])}')

solution = Solution()
print('expect answer [["d"],["ac"]]')
print(f'actual answer {solution.groupAnagrams(["ac", "d"])}')