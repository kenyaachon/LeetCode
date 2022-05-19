from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    def inOrderPrint(self, root: TreeNode) -> None:
        if root == None:
            print(None)
            return
        
        print(root.val)
        self.inOrderPrint(root.left)
        self.inOrderPrint(root.right)

    
    def find_two_swapped(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = y = -1
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                y = nums[i + 1]
                # first swap occurence
                if x == -1:     
                    x = nums[i]
                # second swap occurence
                else:           
                    break
        return [x, y]
        
    def recover(self, root: TreeNode, count: int, x: int, y: int):
        if root:
            if root.val == x or root.val == y:
                root.val = y if root.val == x else x
                count -= 1
                if count == 0:
                    return      
            self.recover(root.left, count, x, y)
            self.recover(root.right, count, x, y)

    def recoverTree(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
            
        nums = self.inorder(root)
        values = self.find_two_swapped(nums)
        x = values[0]
        y = values[1]
        self.recover(root, 2, x, y)


def main():


    
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node1.left = node2
    node2.right = node3
    result = Solution()
    print("Expected output [3, 1, null, null, 2]")
    result.recoverTree(node1)
    result.inOrderPrint(node1)


    node4 = TreeNode(3)
    node5 = TreeNode(1)
    node6 = TreeNode(4)
    node7 = TreeNode(2)
    node4.left = node5
    node4.right = node6
    node6.left = node7
    result = Solution()
    print("Expected output [2, 1, 4, null, null, 3]")
    result.recoverTree(node4)
    result.inOrderPrint(node4)
    

    node8 = TreeNode(1)
    node9 = TreeNode(2)
    node10 = TreeNode(3)
    node11 = TreeNode(4)
    node12 = TreeNode(5)
    node8.left = node9
    node8.right = node12
    node9.left = node10
    node9.right = node11
    result = Solution()
    print("Expected [4, 2, 5, 1, 3]")
    result.recoverTree(node8)
    result.inOrderPrint(node8)

    
if __name__=="__main__":
    main()