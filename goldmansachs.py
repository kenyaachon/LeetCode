"""
An Arry is defined as being in meandering order
when the first 2 elemnts are the respective largest and smallest
elements in the array

>> subssequent elements alternate between its next largest, and next smallest

[first_largest, first_smallest, second_largest, second_smallest...]


i.e
[-1, 1, 2, 3, -5]
sorted normally
[-5, -1, 1, 2, 3]

sorted meandering order
[3, -5, 2, -1, 1]

input: unsorted array

output: array sorted in meandering order

i.e
if array is empty
    return None


note: you can get both positive and negative

possible idea
I could use a max heap for storing the largest
I could use a min heap for storing the smallest 
so I would need to iterate through the unsorted, and add both the
largest and smallest at the same time

while there are still some items in the list
    pop of the heap for largest
    pop of the heap for smallest
    add largest first
    add largest second * -1

return array

possible space complexity o(2N) -> 0(N)
possible time complexity O(n) + ( O(n) * (logn + logn) ) -> O(2nlogn) -> O(nlogn)


a better way is to
sort the array once

then iterate through the sorted array 
    one pointer goes from left to right
    one pointer goes from right to left

"""
from heapq import heapify, heappop, heappush


def meanderingArray(unsorted):
    # Write your code here
    if len(unsorted) == 0:
        return[]
    if len(unsorted) == 1:
        return[unsorted[0]]


    # maxheap = []
    # minheap = []

    # #store the results in a heap
    #     #max heap
    #     #min heap
    # for value in unsorted:
    #     heappush(maxheap, value)
    #     heappush(minheap, -value)

    # #iterate through the heaps
    # #assumption: the heaps are the same size
    # while len(maxheap):
    #     #add largest
    #     #add smallest
    #     result.append(-heappop(minheap))
    #     result.append(heappop(maxheap))
    
    # return result[:len(unsorted)]

    result = []
    # O(nlogn)
    sort = sorted(unsorted)
    

    n = len(sort)

    # O(n)
    for i in range(int(len(sort)/2)):
        result.append(sort[n - 1 - i])
        result.append(sort[i])
    
    if n % 2 !=0:
        result.append(sort[n - int(len(sort)/2 + 1)])
        
        
    return result





unsorted = [5, 2, 7, 8, -2, 25, 25]
# print("expected", [25, -2, 25, 2, 8, 5, 7])
print("actual", meanderingArray(unsorted))

unsorted1 = [-27676, 211621, 904304, 161270, -292822, 732004, 860511, -825806, -721722, 536428, -927571, -287004]
# print("expected", [904304, -927571,
# 860511,
# -825806,
#  732004,
# -721722,
# 536428,
# -292822,
# 211621,
# -287004,
# 161270,
# -27676, ])
print("actual", meanderingArray(unsorted1))