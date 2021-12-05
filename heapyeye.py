from heapq import heapify, heappush, heappop

#create empty heap
heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("The root value of heap : ", str(heap[0]))


print("The heap elements : ")
for i in heap:
    print(i, end=' ')
print('\n')

element = heappop(heap)
print("The heap element :")
for i in heap:
    print(i, end = ' ')
print('\n')

