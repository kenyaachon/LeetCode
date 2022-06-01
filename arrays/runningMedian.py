# class MedianFinder:

#     def __init__(self):
#         #data store
#         self._nums = []
        

#     def addNum(self, num: int) -> None:
#         self._nums.insert(0, num)
#         self._nums.sort()
        

#     def findMedian(self) -> float:
#         print(self._nums)
#         n = len(self._nums)
#         if n == 0:
#             return None
        
#         if n% 2 == 0:
#             middle = int(n/2)
#             first = middle -1
#             # return round(float((self._nums[first]+self._nums[middle])/2), 5)
#             return float((self._nums[first]+self._nums[middle])/2)

#         else:
#             # return round(float(self._nums[int(n/2)]), 5)
#             return float(self._nums[int(n/2)])


from heapq import heappush
import heapq
import time


class MedianFinder:

    def __init__(self):
        #data store
        self._nums = []
        

    def addNum(self, num: int) -> None:
        # self._nums.insert(0, num)
        # self._nums.sort()
        heappush(self._nums, num)
        

    def findMedian(self) -> float:
        n = len(self._nums)
        if n == 0:
            return None
        


        if n %2 == 0:
            middle = int(n/2) + 1
            temp = heapq.nlargest(middle, self._nums.copy())
            return (temp[-1] + temp[-2])/2
        else:
            middle = int(n/2) + 1
            temp = heapq.nlargest(middle, self._nums.copy())
            return temp[-1]

            
        # print(self._nums)
        # if n% 2 == 0:
        #     middle = int(n/2)
        #     first = middle -1
            
        #     return (self._nums[first]+self._nums[middle])/2
        #     # return float((temp[first]+temp[middle])/2)

        # else:
        #     # return float(self._nums[int(n/2)])
        #     temp = sorted(self._nums)
        #     return float(temp[int(n/2)])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
start = time.time()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print("expected 1.5")
print(f"actual {param_2}")
obj.addNum(3)
param_2 = obj.findMedian()
print("expected 2.0")
print(f"actual {param_2}")
print("time taken", time.time() - start)

obj = MedianFinder()
start = time.time()
obj.addNum(2)
obj.addNum(1)
param_2 = obj.findMedian()
print("expected 1.5")
print(f"actual {param_2}")
obj.addNum(4)
param_2 = obj.findMedian()
print("expected 2.0")
print(f"actual {param_2}")
print("time taken", time.time() - start)


obj.addNum(7)
param_2 = obj.findMedian()
print("expected 3.0")
print(f"actual {param_2}")

obj = MedianFinder()
obj.addNum(-1)
print("expected -1")
print(f"actual {obj.findMedian()}")
obj.addNum(-2)
print("expected -1.5")
print(f"actual {obj.findMedian()}")
obj.addNum(-3)
print("expected -2")
print(f"actual {obj.findMedian()}")
obj.addNum(-4)
print("expected -2.5")
print(f"actual {obj.findMedian()}")
obj.addNum(-3)
print("expected -3.0")
print(f"actual {obj.findMedian()}")



