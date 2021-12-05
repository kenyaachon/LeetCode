from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        nodelist = []
        while head:
            nodelist.append(head.val)
            head = head.next
        print(nodelist)

        sum = 0
        sumMap = set()
        for i in range(len(nodelist)):
            for j in range(i, len(nodelist)):
                sum += nodelist[j]
                sumMap.add((j, nodelist[j]))
                if sum == 0:
                    break


            if sum == 0 :
                for value in sumMap:
                    pos, _ = value
                    nodelist[pos] = 10001
            sumMap.clear()
            sum = 0


        if len(nodelist) > 0:
            newHead = ListNode()
            nwHead = newHead
            for i in range(0, len(nodelist)):
                
                if(nodelist[i] != 10001):
                    temp = ListNode(nodelist[i])
                    newHead.next = temp
                    newHead = newHead.next
            return nwHead.next


        return ListNode()


    def printList(self, head: ListNode): 
        while head:
            print(" ->", head.val)
            head = head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(-3)
node4 = ListNode(3)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = Solution()
answer = result.removeZeroSumSublists(node1)
print("expected answer 3,1 or 1,2,1")
print("actual answer", result.printList(answer))
# # print("actual answer", result.printList(node1))


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(-3)
# node5 = ListNode(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# result = Solution()
# answer = result.removeZeroSumSublists(node1)
# print("expected answer 1,2,4")
# print("actual answer", result.printList(answer))
# # print("actual answer", result.printList(node1))


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(-3)
# node5 = ListNode(-2)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# result = Solution()
# answer = result.removeZeroSumSublists(node1)
# print("expected answer 1")
# print("actual answer", result.printList(answer))
# print("actual answer", result.printList(node1))


node1 = ListNode(1)

result = Solution()
answer = result.removeZeroSumSublists(node1)
print("expected answer 1")
print("actual answer", result.printList(answer))