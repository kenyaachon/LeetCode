from bisect import bisect, insort_left
import time
class MedianFinder:

    def __init__(self):
        #data store
        self._nums = []
        

    def addNum(self, num: int) -> None:
        # self._nums.insert(0, num)
        # self._nums.sort()
        insort_left(self._nums, num)

        

    def findMedian(self) -> float:
        # print(self._nums)
        n = len(self._nums)
        if n == 0:
            return None
        
        if n% 2 == 0:
            middle = int(n/2)
            first = middle -1
            # return round(float((self._nums[first]+self._nums[middle])/2), 5)
            return float((self._nums[first]+self._nums[middle])/2)

        else:
            # return round(float(self._nums[int(n/2)]), 5)
            return float(self._nums[int(n/2)])



# from collections import deque
# from heapq import heappush
# import heapq
# import queue
# import time


# class MedianFinder:

#     def __init__(self):
#         #data store
#         self._nums = []
        

#     def addNum(self, num: int) -> None:
#         # self._nums.insert(0, num)
#         # self._nums.sort()
#         heappush(self._nums, num)
        

#     def findMedian(self) -> float:
#         n = len(self._nums)
#         if n == 0:
#             return None
#         if n == 1:
#             return self._nums[0]

#         middlePt = int(n/2)
#         firstPt = middlePt -1
#         middle = 0
#         first = 0

#         queue = deque()
#         queue.append(0)
#         num = 0 

#         for i in range(n):
#             node = queue.popleft()
#             if n%2 == 0:
#                 if num == firstPt:
#                     # first = self._nums[node]
#                     first = node
#             if num == middlePt:
#                 # middle = self._nums[node]
#                 middle = node
#                 break

#             if (2*node+1 < n):
#                 queue.append(2*node+1)
            
#             if (2*node+2 < n):
#                 queue.append(2*node+2)
#             num += 1

            

#             # print(f"middle {middle}")
#             # print(f"first {first}")


#         if n% 2 == 0:

#             return float((self._nums[first]+self._nums[middle])/2)
#         else:
#             return float(self._nums[middle])
        
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



