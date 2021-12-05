# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def recoverTree1(self, root: List[int]) -> None:
        """
        Do not return anything, modify root in-place instead.

        you are given the root of a BST, where the values of exactly two node of the treee were swapped by mistake

        the child of a node for left is index + 1 and for the right is index + 2

        a left child is valid if the it is all smaller than the right child 

        so one solution is to start with the root then check all the way to bottom, and then move on with a new root
        and keep checking until the nodes are valid

        one obvious solution is that instead of chaning the given list we could
        create another and keep inserting the items in the list

        or we could go through the list and check for each to see what is the result
        I am going 
        """

        """
        left: current *2 + 1
        right: current *2 + 2
        
        """

        
        if len(root) == 2:
            if root[0] < root[1]:
                print([root[1], root[0]])
        
        current = 0
        while current < len(root):
            node = current
            while node < len(root):
                left = node * 2 + 1
                right = node * 2 + 2
                if left < len(root) and root[left] != None and root[node] != None:
                    if root[node] < root[left]:
                        #print("before left", root[node], root[left])
                        temp = root[node]
                        root[node] = root[left]
                        root[left] = temp
                        #print("after left", root[node], root[left])
                if right < len(root) and root[right] != None and root[node] != None:
                    if root[node] > root[right]:
                        #print("before right", root[node], root[right])
                        temp = root[node]
                        root[node] = root[right]
                        root[right] = temp
                        #print("after right", root[node], root[right])

                node += 1
            current += 1
    
        print(root)

    def inorderList(self, root: TreeNode) -> List[int]:
        return  [root.val] + self.inorderList(root.left) + self.inorderList(root.right)  if root else [None]


        #check for the right
    def recoverTree(self, root: TreeNode) -> None:
        if root != None:
            input = self.inorderList(root)
            print(input)
            self.recoverTree1(input)
            #self.recovertTreeHelper(root, root, "")


    def recovertTreeHelper(self, root: TreeNode, top: TreeNode, side: str) -> None:
        #check for the left 

        if root.left != None:
            if root.left.val > top.val:
                temp = top.val
                top.val = root.left.val
                root.left.val = temp
                self.recovertTreeHelper(root.left, root.left, "left")
            else:
                self.recovertTreeHelper(root.left, top, "left")
        
        if root.right != None:
            if root.right.val < top.val:
                temp = top.val
                top.val = root.right.val
                root.right.val = temp
                self.recovertTreeHelper(root.right, root.right, "right")
            else:
                self.recovertTreeHelper(root.right, top, "right")
            


    def inOrder(self, root: TreeNode) -> None:
        if root == None:
            return
        
        print(root.val)
        self.inOrder(root.left)
        self.inOrder(root.right)
        


def main():

    
    # input = [1, 3, None, None, 2]
    # result = Solution()
    # print("Expected output [3, 1,null, null, 2]")
    # result.recoverTree1(input)

    # input = [3, 1, 4, None, None, 2]
    # print("Expected output [2, 1, 4, null, null, 3]")
    # result.recoverTree1(input)
    
    

    
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node1.left = node2
    node2.right = node3
    result = Solution()
    print("Expected output [3, 1, null, null, 2]")
    result.recoverTree(node1)
    result.inOrder(node1)


    node4 = TreeNode(3)
    node5 = TreeNode(1)
    node6 = TreeNode(4)
    node7 = TreeNode(2)
    node4.left = node5
    node4.right = node6
    node6.left = node7
    result = Solution()
    print("Expected output [3, 1, 4, null, null, 2]")
    result.recoverTree(node4)
    result.inOrder(node4)
    

    
if __name__=="__main__":
    main()