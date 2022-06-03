"""
You are given an array of integers
Return an array of the same size where the element
at each index is the productof all in the elements
in the original array except for the exceptfor the element
for the elemt at that index


possible way
for each item 
    total
    traverse through the array
        if the current index is safe
            multiple total by current index

    add total to the array

return array

[1, 2, 3, 4, 5] 

total = 2 * 3 * 4 * 5
i = 0
[120, ]

i = 1
total = 1 * 3 * 4* 5
[120, 60]

i = 2
total = 1 * 2  4 * 5


O(n)

so rather than going through the array again
go through the array once
    get all the prefix products

for each index
    total = multiplcate of items before
    only traverse the items after the index
        multiple total by current index
    add total to the array

return array

[1, 2, 3, 4, 5]
[1, 2, 6, 24, 120]

i = 0

prefix = None
total = 2 * 3 * 4 * 5

i = 1
prefix = 1
total = 3 * 4 * 5

"""


"""
Current way
Calculate the prefix and suffix product ahead of time
"""
def products(sum):

    prefix = {}
    suffix = {}
    result = []
    n = len(sum)
    prefix[0] = sum[0]
    suffix[n-1] = sum[-1]
    for i in range(1, n):
        prefix[i] = prefix[i-1] * sum[i]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * sum[i]

    total = 1
    for i in range(n):
        if i - 1 >= 0 and i + 1 < n:
            result.append(prefix[i-1] * suffix[i+1])
        elif i == 0:
            result.append(suffix[1])
        elif i == n - 1:
            result.append(prefix[i-1])
    return result

print (products([1, 2, 3, 4, 5]))

print (products([1,2,3,4]))

print (products([-1,1,0,-3,3]))


