from typing import List


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def insert(self, head: ListNode, size: int) -> ListNode:

        node = head
        for i in range(size):
            head = node
            while(head.next != None):
                print(head.val)
                if(head.val > head.next.val):
                    temp = head.next.val
                    head.next.val = head.val
                    head.val = temp
                    head = head.next
                else:
                    head = head.next

        return node
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        #head = None
        size = 0
        head = lists[0]
        end = lists[0]

        for sublist in lists:
            while sublist != None:
                '''
                temp = sublist.next
                sublist.next = head
                head = sublist
                sublist = temp
                size +=1
                '''
                
                
                temp = sublist.next
                sublist.next = None
                end.next = sublist
                end = end.next
                sublist = temp
                size += 1
                

        
        node = head
        
        for i in range(size):
            head = node
            
            while(head.next != None):
                if(head.val > head.next.val):
                    temp = head.next.val
                    head.next.val = head.val
                    head.val = temp
                    head = head.next
                else:
                    head = head.next
        
        return node
        
    #the faster method for merging 2 lists
    def funfun(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        #head = None
        templist = []
        size = 0
        for sublist in lists:
            while sublist != None:
                templist.append(sublist.val)
                sublist = sublist.next
                size += 1
        

        
        templist = sorted(templist)
        
        Nodes = []
        for i in templist:
            Nodes.append(ListNode(i))
        
        for i in range(size):
            if(i < size - 1):
                Nodes[i].next = Nodes[i + 1]
        
        if (size == 0):
            return None
        else:
            return Nodes[0]
        
        




def main():
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(2)
    node8 = ListNode(6)
    
    node7.next = node8

    input = [node1, node4, node7]
    results = Solution()
    #remedy = results.mergeKLists(input)
    remedy = results.funfun(input)

    
    while(remedy != None):
        print(remedy.val, "->")
        remedy = remedy.next

    
    remedy = results.mergeKLists([None])

    if(remedy == None):
        print("there is nothing")
    
    while(remedy != None):
        print(remedy.val, "->")
        remedy = remedy.next
    
    



if __name__=="__main__":
    main()