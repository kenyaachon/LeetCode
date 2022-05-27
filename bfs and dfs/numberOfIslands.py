from typing import List
from collections import deque

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

    def valid(self, grid, visited, i, j):
        if not (0 <= i < len(grid)):
            return False
        if not (0 <= j < len(grid[i])):
            return False
        if visited[i][j]:
            return False
        return True

    
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 1:
            if len(grid[0]) == 1:
                if grid[0][0] == '1':
                    return 1
                else:
                    return 0
        islands = 0

        column = len(grid[0])
        visited = [[False] * column for i in range(len(grid))]
        neighbors = [[0, -1], [-1, 0],[0, 1], [1, 0]]
        def bfs(i, j):
            print("hello")
            queue = deque()
            queue.append([i, j])
            while len(queue):
                node = queue.popleft()

                visited[node[0]][node[1]] = True
                for adj in neighbors:
                    adjx = node[0] + adj[0]
                    adjy = node[1] + adj[1]
                    if self.valid(grid, visited, adjx, adjy) and grid[adjx][ adjy] != '0':
                        queue.append([adjx, adjy])


        for i in range(len(grid)):
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
print("expected, 1")
print("actual", solution.numIslands([['0']]))