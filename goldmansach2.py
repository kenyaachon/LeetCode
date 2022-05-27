"""

!!NOTE i did look up on python.org anything I didn't remeber about python
subsequence
>> created by deleting zero or more elements from a list while maintain the order

i.e[1,2,3]

subsequences : [1], [2],[3], [1, 2]...

an inversion -> strictly decreasing
subsequence of length 3

i.e 
inversion
p[i] > p[j] > p[k]
i < j < k

i.e
array = [5,3, 4, 2, 1]

inversons:
[5, 3, 2]
[5, 4, 2]
...

n =5
array = [4, 2, 2, 1]

arrays have to be stricly decreasing
so
[4, 2, 2], not valid
but [4, 2, 1] is valid

input: an array
output: a long integer denoting the number of inversons in the array

possible method

best O(nlogn)
sort the array in reverse order

create a hash map 

O(n^2)
for each element in the sorted array
    make a subsequence array which includes sorted[i]
    iterate through the array
        if the subsequence array is smaller than 3
            add the next element to the array if it is not equal to sorted[i]
        else:
            if the subarray is not in the hash map
                add the subarray
            reset the subarray to include only sorted[i] and sorted[j]

return the length of the hashmap

time complexity 
O(n^2) + O(nlogn) -> O(n^2)

space complexity
I = number of inversions
3 -> for the subsequences
3 * O (I) -> O(I)


time 

"""


def maxInversions(arr):
    # Write your code here
    if len(arr) < 3:
        return 0
    
    sortedArr = sorted(arr, reverse=True)

    # possibleInversions = {}
    possibleInversions = set()

    # for each possible element
    for i in range(len(arr)):
        sub = [sortedArr[i]]
        #iterate through the array after index i
        for j in range(i, len(arr)):
            if len(sub) < 3 and sortedArr[j] < sub[-1]:
                sub.append(sortedArr[j])
                print("hit1", i)
                print(sub)
            else:
                # print("hit", i)
                print(sub)
                if (str(sub) not in possibleInversions) and len(sub) == 3:
                    # possibsleInversions[str(sub)] = sub
                    possibleInversions.add(str(sub))
                    # print("hit2")
                
                if sortedArr[j] < sortedArr[i]:
                    sub = [sortedArr[i], sortedArr[j]]
                else:
                    sub = [sortedArr[i]]

        if len(sub) == 3 and str(sub) not in possibleInversions:
            # possibleInversions[str(sub)] = sub
            possibleInversions.add(str(sub))

    # for i in range(len(arr)):
    #     sub = [sortedArr[i]]
    #     for j in range(i, len(arr)):
    #         if sortedArr[j] < sub[-1]:
    #             sub.append(sortedArr[j])
    #             for k in range(j, len(arr)):
    #                 if sortedArr[k] < sub[-1]:
    #                     sub.append(sortedArr[k])
    #                     possibleInversions.add(str(sub))
    #                     sub = sub[:3]

    return len(possibleInversions)
    

print("expected [4, 2, 2, 1], ", 1)
print("actual,", maxInversions([4,2, 2, 1]))

print("expected [5, 4, 3, 2, 1], ", 7)
print("actual,", maxInversions([5, 4, 3, 2, 1]))

print("expected [8, 4, 2, 1], ", 4)
print("actual,", maxInversions([8, 4, 2, 1]))