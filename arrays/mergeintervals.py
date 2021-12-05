from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: (x[0], x[1]))
        print(intervals)

        i = 0
        output = []
        while i < len(intervals):
            first = intervals[i]
            last = [-1, -1]
            smallest = intervals[i][0]
            largest = intervals[i][1]
            j = i
            while j < len(intervals):
                if j + 1 < len(intervals):
                    if largest >= intervals[j+1][0]:
                        if intervals[j+1][1] > largest:
                            largest = intervals[j+1][1]
                        j += 1
                    else:
                        break
                else:
                    break
            output.append([smallest, largest])
            i = j + 1
        return output



# result = Solution()
# answer = result.merge([[1,3],[2,6],[8,10],[15,18]]
# )
# print("expected answer", [[1,6],[8,10],[15,18]])
# print("actual answer", answer)


result = Solution()
answer = result.merge([[1,4],[4,5]])
print("expected answer", [[1,5]])
print("actual answer", answer)

# result = Solution()
# answer = result.merge([[1,4],[2,3]])
# print("expected answer", [[1,4]])
# print("actual answer", answer)


# result = Solution()
# answer = result.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
# print("expected answer", [[1,10]])
# print("actual answer", answer)

# result = Solution()
# answer = result.merge([[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]])
# print("expected answer", [[0,3],[4,6]])
# print("actual answer", answer)