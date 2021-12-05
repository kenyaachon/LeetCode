from typing import List
from collections import deque as queue



class Solution:
    """
    What I am thinking of doing is a bfs search 

    created a second matrix for representing which squares have been visited
    Where I go through the whole matrix
    If I find a character that is the same as the first 
        I check if this character has been visited
        if not then 
            do bfs traversal

    Check if the characteriterator reached the end
        if true, return true
        else return false
    
        
    Go to the bfs traversal of the tree
        Mark the root as visited

        move up to the next character in the target
        check the adjacent coordinates if they equal the current character in the target
            if so add them to the queue


        while the queue is not empty
            traverse the character at the front of the queue



    ex:
    ["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]
    target = ABCCEED


    """

    # def bfsTravsersal(self, visited: List[List[bool]], root, board, target):
    #     rooti, rootj = root
    #     visited[rooti][rootj] = True

    #     que = queue()
    def exist(self, board: List[List[str]], word: str) -> bool:

        single = False
        if len(word) == 1:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == word:
                        single = True
            if single:
                return True

        
        # visited = [[False for words in board] for chara in word ]
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        wordpos = 0
        
        def isValid(visited, adjx, adjy, row, column) -> bool:
            if adjx < 0 or adjy < 0 or  adjx >= row or adjy >= column:
                return False

            if visited[adjx][adjy]:
                return False

            return True

        def bfsTraversal(wordpos, root, adjacent):

            if(len(root) == 0):
                return
            rooti, rootj = root
            visited[rooti][rootj] = True
            # que = queue()
            # que.append(root)

        

            wordpos += 1   
            rows = len(board)
            columns = len(board[0])

            #method that uses backtracing
            # columns = len(board)
            # rows = len(board[0])

            # while len(que) > 0:
            #     newroot = que.popleft()
            #     print("starting the queue")

            #     for sides in adjacent:
            #         newrootx, newrooty = newroot
            #         newrootx += sides[0]
            #         newrooty += sides[1]

            #         if (isValid(visited, newrootx, newrooty, rows, columns) and wordpos < len(word)):
            #             if word[wordpos] == board[newrootx][newrooty]:
            #                 visited[newrootx][newrooty] = True
            #                 que.append((newrootx, newrooty))
            #                 print("current character bfs ", board[newrootx][newrooty], newrootx, newrooty)
            #                 # bfsTraversal(wordpos, (newrootx, newrooty))

            #     if len(que) > 0:
            #         godown = que.popleft()
            #         wordpos = bfsTraversal(wordpos, godown, adjacent)
            for sides in adjacent:
                newrootx, newrooty = root
                newrootx += sides[0]
                newrooty += sides[1]

                if (isValid(visited, newrootx, newrooty, rows, columns) and wordpos < len(word)):
                    # print("current character bfs ", board[newrootx][newrooty], newrootx, newrooty)

                    if word[wordpos] == board[newrootx][newrooty]:
                        print("wordpos", wordpos)
                        # visited[newrootx][newrooty] = True
                        print("root character bfs ", board[rooti][rootj], newrootx, newrooty)

                        print("current character bfs ", board[newrootx][newrooty], newrootx, newrooty)
                        wordpos = bfsTraversal(wordpos, (newrootx, newrooty), adjacent)

            return wordpos
        
        def traverse(adjacent, wordpos) -> bool:
            for i in range(len(visited)):
                for j in range(len(visited[i])):
                    if visited[i][j] == False and wordpos < len(word):
                        if board[i][j] == word[wordpos]:
                            print("current character", board[i][j])
                            wordpos = bfsTraversal(wordpos, (i,j), adjacent)

                            if wordpos == len(word):
                                return True
                            wordpos = 0
            return False

        straight = [[-1,0], [0,-1], [1, 0], [0, 1]]
        diagonal = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

        if traverse(straight, 0):
            return True
        # else:
        #     visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        #     return traverse(diagonal, 0)
        return False



result = Solution()
# answer = result.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
# print("expected answer True")
# print("actual answer,", answer)

# answer = result.exist([["a"]], word = "a")
# print("expected answer True")
# print("actual answer,", answer)

# answer = result.exist([["a", "a"]], word = "a")
# print("expected answer True")
# print("actual answer,", answer)

# answer = result.exist([["a","b"],["c","d"]], word="abcd")
# print("expected answer False")
# print("actual answer", answer)

# answer = result.exist([["C","A","A"],["A","A","A"],["B","C","D"]], word ="AAB")
# print("expected answer True")
# print("actual answer", answer)



# answer = result.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
# print("expected answer True")
# print("actual answer,", answer)



# answer = result.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
# print("expected answer False")
# print("actual answer,", answer)


answer = result.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
print("expected answer True")
print("actual answer,", answer)

# print(len("ABCESEEEFS"))
