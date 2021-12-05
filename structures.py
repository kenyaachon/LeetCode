import heapq
from typing import List
class Solutions:
    def minMeetinngRoomsHeap(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = []
        intervals.sort(key = lambda x: x[0])

        heapq.heappush(rooms, intervals[0][1])


        for meeting in intervals[1:]:

            print(meeting)
            print(rooms)
            if rooms[0] <= meeting[0]:
                heapq.heappop(rooms)


            heapq.heappush(rooms, meeting[1])

        print(rooms)
        return len(rooms)
        

def main():
    answers = Solutions()
    input = [[15,16],[10,15],[16,25]]
    result = answers.minMeetinngRoomsHeap(input)
    print("expected: 1")
    print(result)

    input = [[20,45],[12,13],[2,50],[14,20],[3,5]]
    result = answers.minMeetinngRoomsHeap(input)
    print("expected: 2")
    print(result)

    input = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    result = answers.minMeetinngRoomsHeap(input)
    print("expected: 2")
    print(result)

if __name__=="__main__":
    main()

'''
A fibionacci heap is a data structure that consists of a collection which will follow min heap 
or max heap property. We have already discuss min heap and max heap property in the Heap Data Structure article
These two properties are the characterisitcs of the trees present on a fibonacci heap

In a fibonacci heap, a node can have more than two children or no children at all.
Also, it has more efficient heap operations than that supported by the binomial and binary heaps

A fibonacci heap is called a fibonacci heap because the trees are constructured in a way such that a tree of order n
has at least Fn+2 nodes in it, where Fn+2 is the (n+2)th Fibonacci number

Properties of a Fibonacci Heap
important properties of a Fibonaccci heap are:
1. it is a set of min-heap-ordered trees. So the parent is always smaller than the children
2. A pointer is maintained at the minimum element node
3. It consists of a set of marked nodes. Decrease Key operation
4. The trees within a Fibonacci heap are unordered but rooted

The roots of all the trees are linked together for faster access. The child nodes of a parent node
are connected to each other through a circulay doubly linked list as shown below/

There are two main disadvantages of using a circular doubly linked list
1. Deleting a node from the tree takes o(1) time
2. The concatenation of two such lists takes 0(1) time

insertion
Algorithm
insert(Heap, x)
    degree[x] = 0
    parent[x] = NIL
    child[x] = NIL
    left[x] = x
    right[x] = x
    mark[x] = FALSE
    concatenate the root list containing x with root list Heap
    if min[Heap] == NIL, or key[x] < key[min[Heap]]
        then min[H] = x
    n[H] = n[H] + 1

inserting a node into an already existing heap follows the steps below
1. Create a new node for the element
2. Check if the heap is empty
3. If the heap is empty, set the new node as a root node andd mark it min
4. else, insert the node into root list and update min

Find Min
The minimum element is always given by the min pointer

Union
Union of two fibonacci heaps consists of following steps

1. Update min by selecting a minimum key from the new root lists

Extract min
it is the most important operation on a fibonacci heap.In this operation, the node with minimum value is removed from the heap and three
is re-adjusted
1. Delete the min node
2. Set the min-pointer to the next root in the root list
3. Create an array of size equal to the maximum degree of the trees in the heap before deletion
4. Do the following steps 507, until there are no multiple roots with the same degree
5. Map the dgree of current root(min-pointer) to the degree in the array
6. Map the degree of next root to the degree in array
7. If there are more than 2 mappings for the same degree, then apply union operation to those roots such that the min-heap property
is maintained(i.e the minimum is at the root)

FIB-HEAP-INSERT(H, X)
x.degree = 0
x.p = NIL
x.child = NIL
x.mark = FALSE
if H.min == NIL
    #create a root list for H containing just x
    H.min = x
else insert x into H's root list
    if x.key < H.min.key
        H.min = x
H.n = H.n + 1

FIB-HEAP-UNION(Heap1, Heap2)
H = MAKE-FIB-HEAP()
H.min = H1.min
#concate the root list of H2 with the root list of H:
if(H1.min == NIL) or (H2.min != NIL and H2.min.key < H1.min.key)
    H.min = H2.min
H.n = H1.n + H2.n
return H

FIB-HEAP-EXTRACT-MIN(H):
z = H.min
if z != NIL
    for each child x of z
        add x to the root list of H
        x.p = NIL
    remove z from the root list of H
    if z == z.right
        H.min = NIL
    else
        H.min = z.right
        CONSOLIDATE(H)
    H.n = H.n - 1
return z

CONSOLIDATE(H):
let A[0..D(H.n)] be a new array
for i = o to D(H.n)
    A[i] = NIL
for each node w in the root list of H
    x = w
    d = x.degree
    while A[d] != NIL   
        y = A[d]
        if x.key > y.key
            exchange x with y
        FIB-HEAP-LINK(H, y, x)
        A[d] = NIL
        d = d + 1
    A[d] = x
H.min = NIL
for i =0 to D(H.n)
    if A[i] != NIL
        if H.min == NIL 
            create a root list for H continaing just A[i]
            H.min = A[i]
        else
            insert A[i] into H's root list
                if A[i].key < H.min.key
                    H.min = A[i]

FIB-HEAP-LINK(H, y, x)
remove y from the root list of H
make y a child of x, incrementing x.degree
y.mark = False

FIB-HEAP-DECREASE-KEY(H, x, k)
if k > x.key
    erro "new key is greater than currenty key"
x.key = k
y = x.p
if y != NIL and x.key < y.key
    CUT(H, x, y)
    CASCADING-CUT(H,y)
if x.key < H.min.key
    H.min = x

CUT(H, x, y)
remove x from the child list of y, decrementing y.degree
add x to the root list of H
x.p = NIL
x.mark = FALSE

CASCADING-CUT(H, y)
z = y.p
if z != NIL
    if y.mark == FALSE
        y.mark = TRUE
    else 
        CUT(H, y, z)
        CASCADING-CUT(H, Z)

'''
import math

#creating fibonacci tree
class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    #Adding tree at the end of the tree
    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order  + 1


class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0
    
    #insert a node
    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count += 1

    #get minimum value
    def get_min(self):
        if self.least is None:
            return None
        return self.least.value

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            
            self.count -= 1
            return smallest.value
    
    #consolidate the tree
    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None or k.value < self.least.value):
                    self.least = k

def floor_log(x):
    return math.frexp(x)[1] - 1

def main1():

    fibonacci_heap = FibonacciHeap()

    fibonacci_heap.insert_node(7)
    fibonacci_heap.insert_node(3)
    fibonacci_heap.insert_node(17)
    fibonacci_heap.insert_node(24)

    print('the minimum value of the fibonacci heap: {}'.format(fibonacci_heap.get_min()))

    print('the minimum value removed: {}'.format(fibonacci_heap.extract_min()))

if __name__=="__main__":
    main1()

    
    