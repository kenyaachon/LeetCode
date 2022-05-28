from typing import List
from collections import deque
import time

"""
islands is surrounded by water and is formed by connecting
 adjacent lands horizontally or vertically

you may assume all four edges of the grid are surrounded by water

'1' - land
'0' - water

input: 2d binary grid

output: the number of islands

"""
class Solution:

    def valid(self, grid, i, j):
        if not (0 <= i < len(grid)):
            return False
        if not (0 <= j < len(grid[i])):
            return False
        return True

    
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        if row == 1 and column == 1:
            if grid[0][0] == '1':
                return 1
            else:
                return 0
        islands = 0

        visited = [[False] * column for i in range(row)]
        neighbors = [[0, -1], [-1, 0],[0, 1], [1, 0]]
        queue = deque()

        def valid(i, j):
            if not (0 <= i < row):
                return False
            if not (0 <= j < column):
                return False
            return True


        def bfs(i, j):
            queue.append([i, j])
            while len(queue):
                node = queue.popleft()

                visited[node[0]][node[1]] = True
                for adj in neighbors:

                    adjx = node[0] + adj[0]
                    adjy = node[1] + adj[1]
                    if valid(adjx, adjy):
                    # if self.valid(grid, adjx, adjy):
                        if  not visited[adjx][adjy] and (grid[adjx][adjy] == '1'):
                            visited[adjx][adjy] = True

                            queue.append([adjx, adjy])


        for i in range(row):
            for j in range(column):
                if not visited[i][j] and grid[i][j] != '0':
                    bfs(i, j)
                    islands += 1

        return islands

# map = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# solution = Solution()
# print("expected, 1")
# print("actual", solution.numIslands(map))

map = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


solution = Solution()
print("expected, 3")
print("actual", solution.numIslands(map))



solution = Solution()
print("expected, 1")
print("actual", solution.numIslands([['1']]))

solution = Solution()
print("expected, 0")
print("actual", solution.numIslands([['0']]))

map = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
solution = Solution()
print("expect, something")
start = time.time()
print("actual", solution.numIslands(map))
end = time.time()
print("time to execute", end-start)
