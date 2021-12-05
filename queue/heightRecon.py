from typing import List


class Solution:

    """
    
    so for one example it would be
    [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

    [4,0], [5,0], [3,2], [2,2], [1,4] [6,0]

    ok so you only starting counting the number of people in front only from the
    the tallest back to current position 


    what I am thinking is that I might need to take multiple passes in order to full
    construct the queue
    Initial thought was that it was like just sorting a list first by the second number, then by 
    the third number if there is a tie


    for the first look I want to find the biggest items

    for the second look I want to insert the items in the list,


    *as I am going through the list I will remove the item from the list to make sure I am not having duplicates


    [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

    [5,0] [6,1] [5,2] [7,0] [4,4] [7,1]



    for each person in list:
        insertPersonToList(list, person)


    insertPersonToList(List, person):
        kCount = 0
        lastPos = 0
        if len(list) == 0:
            append person to user
            exit from function

        if person.ki == 0:
            while person.height > next person.height:
                lastPos += 1

        while kCount <= person.ki and lastPos < len(list) - 1:
            if List item.height >= person.height:
                kCount += 1
            lastPos += 1

        
        if lastPos + 1 >= len(list):
            append person to end
        otherwise:
            insertPerson(lastPos, person)
            
    
    ex:
    [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

    [7,0]
    [7,0][4,4]
    [5,0][7,0][4,4][7,1]
    



    """
    def insertPeople(self, people: List[List[int]], person):
        print("Hello people")
        print(person)
        kCount = 0
        lastPos = 0
        if len(people) == 0:
            people.append(person)
            return

        if person[1] == 0:
            while lastPos < len(people):
                if people[lastPos][0] < person[0]:
                    lastPos += 1
                    kCount += 1
                else: 
                    break
            people.insert(lastPos, person)
            return
            
        while kCount <= person[1] and lastPos < len(people):
            if people[lastPos][0] >= person[0]:
                kCount += 1

            # else:
            #     if people[lastPos][1] >= person[1] and kCount == person[1]:
            #         break
            lastPos += 1

        # if lastPos + 1 >= len(people):
        #     people.append(person)
        # else:
        people.insert(lastPos, person)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        newQue = []

        # people.sort(key = lambda x: (-x[0], x[1]))
        # # for person in people:
        # #     self.insertPeople(newQue, person)



        people.sort(key = lambda x: (-x[0], x[1]))
        # people.sort(key = lambda x: (x[1], -x[0]))
        print(people)
        for person in people:
            newQue.insert(person[1], person)

        return newQue


result = Solution()
# answer = result.reconstructQueue([[7,0],[4,4],[7,1], [6,1]])
answer = result.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
# answer = result.reconstructQueue([[7,0],[4,4],[7,1],[5,0]])

print("expected answeer ", [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])
print("actual answer    ", answer)