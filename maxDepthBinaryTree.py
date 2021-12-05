# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    if root is null 
        return the height 0

    else if root has no children
        return the height 1

    return the maxDepthHelper


    so create a maxDepthHelper
    it takes in the root, and the current height
    if the root is null
        return the height
    
    increment the height
    return the max of the left and right node



    
    """
    def maxDepthHelper(self, root: TreeNode, height: int) -> int:
        if root is None:
            return height
        
        height += 1
        return max(self.maxDepthHelper(root.left, height), 
        self.maxDepthHelper(root.right, height))
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1

        
        return self.maxDepthHelper(root, 0) 



def main():

    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 =  TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    solution = Solution()
    result = solution.maxDepth(node1)
    print("Actual result", result)
    print("Expected Result 3")


    node6 = TreeNode(1)
    node7 = TreeNode(2)
    node6.right = node7
    result = solution.maxDepth(node6)
    print("Actual result ", result)
    print("Expected result 2 ")

    result = solution.maxDepth(None)
    print("Actual result ", result)
    print("Expected result 0")

    node9 = TreeNode(0)
    result = solution.maxDepth(node9)
    print("Actual result ", result)
    print("Expected result 1")



if __name__ =="__main__":
    main()