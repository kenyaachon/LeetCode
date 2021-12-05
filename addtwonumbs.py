# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def convertListToInt(self, list: ListNode) -> int:

        num = ''
    
        while(list != None):
            num = str(list.val) + num
            list = list.next

        return int(num)

    def convertIntToList(self, result) -> ListNode:
        
        list = None
        for char in result:
            tempNode = ListNode(int(char))
            tempNode.next = list
            list = tempNode
            print(char)

        return list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1num = self.convertListToInt(l1)
        l2num = self.convertListToInt(l2)

        sum = l1num + l2num
        result = str(sum)

        return self.convertIntToList(result)



    def main(self): 

        print("main")
        node1 = ListNode(2)
        node2 = ListNode(4)
        node3 = ListNode(3)

        node1.next = node2
        node2.next = node3

        nodea = ListNode(5)
        nodeb = ListNode(6)
        nodec = ListNode(4)

        nodea.next = nodeb
        nodeb.next = nodec

        result = self.addTwoNumbers(node1, nodea)
        
        while(result):
            print(result.val, "->")
            result = result.next
            #result = ListNode()



if __name__ =="__main__":
    newList = Solution()
    newList.main()

        