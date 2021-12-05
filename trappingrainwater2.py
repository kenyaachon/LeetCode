


"""
[3, 3, 3, 3, 3]
[3, 2, 2, 2, 3]
[3, 2, 1, 2, 3]
[3, 2, 2, 2, 3]
[3, 3, 3, 3, 3]

so the borders of the matrix don't matter in terms of looking at them
I want to look at the inner part of the matrix to see whether 

I am thinking to compare the current cell with the adjacent cells,
then I want to see which of the cells have min
then I do the following operation ans += min cell - current cell 

so for each 2d elevation map
we are going to find the highest points

then after we have a new matrix with the highest points
for each inner cell we compare each adjacent cell to see which cell is the min
then from the min adjacent we will minus it against the current cell and add the result to the total ans

ex
[3, 3, 3, 3, 3]
[3, 2, 2, 2, 3]
[3, 2, 1, 2, 3]
[3, 2, 2, 2, 3]
[3, 3, 3, 3, 3]
the new matrix would be

[3, 3, 3, 3, 3]
[3, 3, 3, 3, 3]
[3, 3, 3, 3, 3]
[3, 3, 3, 3, 3]
[3, 3, 3, 3, 3]

[ 0, 0, 0, 0, 0]
[ 0, 1, 1, 1, 0]
[ 0, 1, 2, 1, 0]
[ 0, 1, 1, 1, 0]
[ 0, 0, 0, 0, 0]
ans = 10



"""
from typing import List
from collections import deque as queue


class Solution:

    def findHighestPt(self, heightMap: List[int]):
        if(len(heightMap) == 0):
            return []
        size = len(heightMap)
        leftMax = [0 for i in range(size + 1)]
        rightMax = [0 for i in range(size + 1)]
        #leftMax = []
        #rightMax = []
        #leftMax.append(heightMap[0])
        leftMax[0] = heightMap[0]
        result = []
        for i in range(0, size):
            leftMax[i] = max(heightMap[i], leftMax[i-1])
            #leftMax.insert(i, max(heightMap[i], leftMax[i-1]))

        for i in reversed(range(0, size)):
            rightMax[i] = max(heightMap[i], rightMax[i+1])
            #rightMax.insert(i, max(heightMap[i], rightMax[i+1]))

        for i in range(size):
            result.append(min(leftMax[i], rightMax[i]))
            #result.append(rightMax[i])
            #result.insert(i, rightMax[i])

        return result

    def isValid(self, visited, row, column, rowSize, ColumnSize):
        if row < 0 or column < 0 or row >= rowSize or column >= ColumnSize:
            return False

        
        if (visited[row][column]):
            return False

        return True

    def helperTrap(self, heightMap: List[List[int]], newMatrix: List[List[int]]) -> int:
        ans = 0
        # Direction vectors
        dRow = [ -1, 0, 1, 0]
        dCol = [ 0, 1, 0, -1]

        row = len(heightMap)
        column = len(heightMap[0]) 
        # Declare the visited array
        visited = [[ False for i in range(column)] for i in range(row)]

        que = queue()

        #start at the beginning of the queue
        que.append((0, 0))
        visited[0][0] = True

        

        #Do a BFS traversal of the height Matrix
        while(len(que) > 0):
            cell = que.popleft()
            xCoordinate = cell[0]
            yCoordinate = cell[1]

            min = [xCoordinate + dRow[0], yCoordinate + dCol[0]]
            for i in range(4):
                adjx = xCoordinate + dRow[i]
                adjy = yCoordinate + dCol[i]

                #print("row", row)      
                #print("column", column)
                #print("x", adjx)
                #print("y", adjy)          
                if(self.isValid(visited, adjx, adjy, row, column)):
                    if newMatrix[adjx][adjy] < newMatrix[min[0]][min[1]]:
                        min = [adjx, adjy]
                    
                    que.append((adjx, adjy))
                    visited[adjx][adjy] = True
            if xCoordinate == 0 or yCoordinate == 0 or xCoordinate == row - 1 or yCoordinate == column - 1:
                continue
            else:
                ans += newMatrix[min[0]][min[1]] - heightMap[xCoordinate][yCoordinate]
        return ans


    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2:
            return 0
        
        newMatrix = []
        for map in heightMap:
            result = self.findHighestPt(map)
            print(result)
            newMatrix.append(result)

        #do a BFS traversal of heightMap and compare against the New Matrix
        return self.helperTrap(heightMap, newMatrix)
    

        


def main():
    print("hello")
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    answers = Solution()
    result = answers.trapRainWater(heightMap)
    print("expected: 4")
    print("output:", result)

    heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    result = answers.trapRainWater(heightMap)
    print("expected: 10")
    print("output:", result)

    heightMap = [[1,3,3,1,3,2],[3,2,1,3,2,3],[3,3,3,2,3,1]]
    result = answers.trapRainWater(heightMap)
    print("expected: 4")
    print("output:", result)

    heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    result = answers.trapRainWater(heightMap)
    print("expected: 14")
    print("output:", result)


if __name__=="__main__":
    main()