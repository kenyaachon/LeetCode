"""
given n non-negative ints representing an elevation map 
each bar width is, computer how much water it can trap after raining

water can be held when there is a space between 2 elevations

height of the water is determined by the lowest elevation
we can compare more than one elevation to get the elevation height



input 4, 2, 0, 3, 2, 5


          x
x 0 0        x 
x 0 0   x   x 
x x 0  x x x
x x 0 x x x

"""
from typing import ItemsView, List



class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        #check if the elevation is complete
        if len(height) <= 2:
            return 0

        lastTallest = height[0]
        nextItem = 1
        #iterate through the elevation map
        while nextItem < len(height):
            print("position " , nextItem," nextItemvalue", height[nextItem])
            if height[nextItem] >= lastTallest:
                lastTallest = height[nextItem]
            else:
                nextItem2 = nextItem
                temp = 0
                notChanged = True
                #traverse the elevation map until we find another tall elevation
                while nextItem2 < len(height):
                    nextItem2Value = height[nextItem2]
                    print("elevation", nextItem2Value)
                    if lastTallest > nextItem2Value:
                        elevationDiff = lastTallest - nextItem2Value
                        temp += elevationDiff
                        print("tempSum After change", temp)
                        nextItem2 += 1
                    #stop counting the water units once we see the elevation is too high
                    elif lastTallest <= nextItem2Value:
                        lastTallest = nextItem2Value
                        nextItem = nextItem2 - 1
                        notChanged = False
                        #adding the size for the smaller problem to the larger problem
                        print("result for subproblem", temp)
                        total += temp
                        print("total after addition", total)
                        break

                if notChanged:
                    lastTallest = height[nextItem]


                
            nextItem += 1
        return total
    def peek(self, myStack):
        if len(myStack) == 0:
            return 0
        return myStack[len(myStack) - 1]
    
    def soltap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        myStack = []



        while(current < len(height)):
            print(myStack)
            
            #check for the lower elevations that can hold water
            while(len(myStack) > 0 and (height[current] > height[self.peek(myStack)]) ):
                top = self.peek(myStack)
                myStack.pop()
                if(len(myStack) == 0):
                    break
                distance = current - self.peek(myStack) - 1
                bounded_height = min(height[current], height[self.peek(myStack)]) - height[top]
                ans += distance * bounded_height
                print("distance", distance)
                print("bounded_height", bounded_height)
            
            myStack.append(current)
            current += 1


        return ans

def main():
    example = Solution()


    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    #result = example.trap(input)
    #print("Output: ", result)
    #print("Expected: 6")

    input2 = [4,2,0,3,2,5]
    #result = example.trap(input2)
    #print("Output: ", result)
    #print("Expected: 9")

    input2 = [4,2,3]
    #result = example.trap(input2)
    #print("Output: ", result)
    #print("Expected: 1")


    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = example.soltap(input)
    print("Output: ", result)
    print("Expected: 6")

    input2 = [4,2,0,3,2,5]
    result = example.soltap(input2)
    print("Output: ", result)
    print("Expected: 9")

    input2 = [4,2,3]
    result = example.soltap(input2)
    print("Output: ", result)
    print("Expected: 1")



if __name__=="__main__":
    main()