"""

for each internaval
    add up the end and start
    if the current interval is equal or greater than the previous interval
        then increment the number of rooms
        then set the previous to the current

[[1,5],[8,9]]
rooms = 1

[[1, 9], [3, 15], [9, 16], [6, 16]]
rooms = 3

[[4, 9], [9, 10], [4, 17]]
rooms = 2

[[2, 11], [6, 16], [11, 16]]
rooms = 2

[[5, 8], [6, 8]]
rooms = 2

[[6, 15], [6, 17], [13, 20]]
rooms = 3

[[6, 10], [13, 14], [12, 14]]
rooms = 2

when counting the number of rooms
you need more rooms when
when one meeting is happening at the same exact time
when one meeting starts before another


you don't need additional rooms when 
a meeting happens after another meeting ends

the challenge is that the meeting times that are right after can be anywherein the list
even if we sort it

say for the list 
[[1, 9], [3, 15], [9, 16], [6, 16]]

[[3,5], [6, 16]]

[1,9]: [9, 16]
[3,5]: 
[6, 16;
rooms 3


[[1, 5], [8, 9], [8, 9]]

[1,5]: [8,9]
[8,9]: 
rooms 2

[[6, 15], [6, 17], [13, 20]]

[6,15]: 
[6,17]:
[13,20]:
rooms


[[2,15],[36,45],[9,29],[16,23],[4,9]]
[[4, 9], [2, 15], [16, 23], [9, 29], [36, 45]]
[4,9]: [9, 29]
[2, 15]: [16, 23], [36, 45]

or
[4,9]: [16, 23], [36, 45]

sort the list of intervals

for each intervalA in the list
    create list for intervalA
    compare with the other intervalsB
        if an intervalB is after interval B
            add intervalB to the list for interval B
            remove interval B from the list
        else if an intervalB is exactly same as the intervalB
            remove intervalB from the list
            create own list for IntervalB


count the number of lists 


"""

'''
        for intervalA in result:
            temp = []
            temp.append(intervalA)
            result.remove(intervalA)

            #print("intervalA removal", result)
            print("intervalA", intervalA)
            
            
            for intervalB in result:
                if intervalB[0] >= intervalA[1]:
                    temp.append(intervalB)
                    result.remove(intervalB)
                elif intervalB[0] == intervalA[0] and intervalB[1] == intervalA[1]:
                    schedule.append(intervalB)
                    result.remove(intervalB)

                #intervalA = intervalB
                
                if len(result) == 1:
                    if result[0][0] >= intervalB[1]:
                        temp.append(result[0])
                    else:
                        schedule.append(result[0])
                    

            #print("intervalB", result)
            schedule.append(temp)
'''
from typing import List
import heapq

class Solution:
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms

    def minMeetinngRoomsHeap(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = []
        intervals.sort(key = lambda x: x[0])

        heapq.heappush(rooms, intervals[0])


        for meeting in intervals[1:]:

            if rooms[0] <= meeting[0]:
                heapq.heappop(rooms)


            heapq.heappush(rooms, meeting[1])

        return rooms
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        result = sorted(intervals, key=lambda x: x[1])

        print(result)
        schedule = []
        i = 0

        start = 0
        j = 0
        #for j in range(start, len(result)):
        while 0 < len(result):
            intervalA = result[j]
            temp = []
            temp.append(intervalA)
            result.remove(intervalA)
            #print("before", schedule)
            #print("interval", intervalA)
            
            i = 0
            while i < len(result):                
                intervalB = result[i]
                print("intervalB", "i", i, intervalB)

                    
                if intervalB[0] >= intervalA[1]:
                    temp.append(intervalB)
                    result.remove(intervalB)
                    intervalA = intervalB
                    i -= 1

                elif intervalB[0] == intervalA[0] and intervalB[1] == intervalA[1]:
                    schedule.append(intervalB)
                    result.remove(intervalB)   
                    #i -= 1
                    



                i += 1 
                print(result)
                
                if len(result) == 1:
                    if result[0][0] >= intervalB[1]:
                        temp.append(result[0])
                        result.remove(result[0])
                    else:
                        schedule.append(result[0])
                        result.remove(result[0])  
                          

                         

            schedule.append(temp)
        
        print("done", schedule)
        
        return len(schedule)
        

'''
            size = len(result)

            i +=1

            for i in range(i, size):
                if result[i][0] >= intervalA[1]:
                    temp.append(result[i])
                    result.remove(result[i])
                elif result[i][0] == intervalA[0] and result[i][1] == intervalA[1]:
                    schedule.append(result[i])
                    result.remove(result[i])
'''

def main():
    input = [[0,30],[5,10],[15,20]]
    #input = [[0,30],[15,20]]
    answers = Solution()

    
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    
    input = [[7,10],[2,4]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 1")
    print(result)

    input = [[1,5],[8,9]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 1")
    print(result)

    input = [[5,8],[6,8]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    input = [[13,15],[1,13]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 1")
    print(result)


    
    input = [[2,11],[6,16],[11,16]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)
    

    input = [[6,15],[13,20],[6,17]]
    answers = Solution()
    result = answers.minMeetingRooms(input)
    print("expected: 3")
    print(result)

    input = [[9,10],[4,9],[4,17]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    input = [[9,16],[6,16],[1,9],[3,15]]
    result = answers.minMeetingRooms(input)
    print("expected: 3")
    print(result)
    


    input = [[13,15],[1,13],[6,9]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)
    

    input = [[6,10],[13,14],[12,14]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    

    input = [[2,5],[3,14],[12,17],[4,11]]
    result = answers.minMeetingRooms(input)
    print("expected: 3")
    print(result)

    input = [[1,5],[8,9],[8,9]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    input = [[2,6],[12,18],[9,18],[15,20]]
    result = answers.minMeetingRooms(input)
    print("expected: 3")
    print(result)

    
    input = [[4,16],[5,17],[4,17],[12,17]]
    result = answers.minMeetingRooms(input)
    print("expected: 4")
    print(result)

    input = [[15,16],[10,15],[16,25]]
    result = answers.minMeetingRooms(input)
    print("expected: 1")
    print(result)

    input = [[20,45],[12,13],[2,50],[14,20],[3,5]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)

    input = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    result = answers.minMeetingRooms(input)
    print("expected: 2")
    print(result)



if __name__=="__main__":
    main()