def heapify(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and array[i] < array[left]:
        largest = left

    if right < size and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, size, largest)

    
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)

    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size  - 1], array[i]

    array.remove(num)
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

def main():
    array = []

    insert(array, 3)
    insert(array, 4)
    insert(array, 9)
    insert(array, 2)

    print ("Max-Heap array: " + str(array))

    deleteNode(array, 4)
    print("After deleting an element: " + str(array))


if __name__=="__main__":
    main()