
"""
reverse the order of characters in each word
*preserve whitespace and initial word
order

The cat in the hat
ehT tac ni eht tah



The
eht


cat
tac


"cat "
possible way
I seperate out the words by dividing them between spaces

calculate the number of space
    -> space = number of words - 1

total word
for each word in the string
    reverse the word
    add the reverseword + space

truncate the string for extra spaces

return total word

this will use O(h) space
this will take O(h) time
h -> number of words

example


The cat in the hat
parse by " "
[The, cat, in, the, hat]

h = 5
space = h - 1 = 4

eht 
eht tac 
eht tac ni 

I seperate out the words by dividing them between spaces

calculate the number of space
    -> space = number of words - 1

total word
for each word in the string
    reverse the word
    add the reverseword + space

truncate the string for extra spaces

return total word

this will use O(h) space
this will take O(h) time
h -> number of words
"""
import string


# class Solution:
#   def reverseWords(self, str):
#     # Fill this in.å
#     words = str.split(" ")
#     space = len(words) - 1
#     totalword = ""
#     for word in words:
#         if space > 0:
#             totalword += word[::-1] + " "
#             space -= 1
#         else:
#             totalword += word

#     return totalword

# print(Solution().reverseWords("The cat in the hat"))

class Solution:
  def reverseWords(self, str):
    # Fill this in.å
    if len(str) == 1:
        return str

    words = str.split()[::-1]
    print(words)
    space = len(words) - 1
    totalword = ""
    for word in words:
        if space > 0:
            totalword += word + " "
            space -= 1
        else:
            totalword += word

    return totalword

print(Solution().reverseWords("The cat in the hat"))

print(Solution().reverseWords("the sky is blue"))

print(Solution().reverseWords("  hello world  "))

print(Solution().reverseWords("a good   example"))


print(Solution().reverseWords("the-sky is blue"))

