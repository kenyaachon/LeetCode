import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__k = k
        self.__minheap = []

        if len(nums) == 0:
            return


        for item in nums:
            if len(self.__minheap) < k:
                heapq.heappush(self.__minheap, item )

            else:
                if item > self.__minheap[0]:
                    heapq.heappop(self.__minheap)
                    heapq.heappush(self.__minheap, item)


    def add(self, val: int) -> int:
        if len(self.__minheap) == 0:
            heapq.heappush(self.__minheap, val)
        elif(len(self.__minheap) < self.__k):
            heapq.heappush(self.__minheap, val)
        elif(val > self.__minheap[0]):
            heapq.heappop(self.__minheap)
            heapq.heappush(self.__minheap, val)


        print(self.__minheap)
    
        return self.__minheap[0]
        



def main():
    
    
    solution = KthLargest(2, [0])
    result = solution.add(-1)
    print("expexted", -1)
    print("output", result)

    result = solution.add(1)
    print("expexted", 0)
    print("output", result)

    result = solution.add(-2)
    print("expexted", 0)
    print("output", result)

    result = solution.add(-4)
    print("expexted", 0)
    print("output", result)
    
    result = solution.add(3)
    print("expexted", 1)
    print("output", result)
    


if __name__=="__main__":
    main()