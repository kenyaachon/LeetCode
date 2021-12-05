# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:

        # if root is None:
        #     return 

        # if root.right is None and root.left is None:
        #     return True
        # if root.left:
        #     if root.val < root.left.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left)
        # if root.right:
        #     if root.val > root.right.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.right)
        
        # return True

        if root is None:
            return True
        if root.left is None and root.right is None:
            return  True
        
        if root.left:
            print("hit left")
            if root.val <= root.left.val:
                return False
            self.isValidBST(root.left)
        if root.right:
            print("hit right")
            if root.val >= root.right.val:
                return False
            self.isValidBST(root.right)

        return True

    def bstValidator(self, rangeBST: tuple) -> bool:
        left, root, right = rangeBST
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        
        # leftVal = left if left is TreeNode else left.val
        # rightVal = right.val if right is TreeNode else right
        
        tempRight = right

        if left.val > root.val:
            right = left
            left.val = -math.inf
        elif root.val > right.val:
            left = right
            right.val = math.inf

        print("left %d root %d right %d", left.val, root.val, right.val)

        if root.left:
            if root.left.val <= left.val or root.left.val >= root.val:
                print("printed a false on left")
                return False
            else:
                self.bstValidator((TreeNode(-math.inf), root.left, tempRight))
        if root.right:
            if root.right.val <= root.val or root.right.val >= right.val:
                print("printed a false on right")
                return False
            else:
                self.bstValidator((root, root.right, TreeNode(math.inf)))


    def isValidBST(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True

        if root.right:
            if root.right.val <= root.val:
                return False
        if root.left:
            if root.left.val >= root.val:
                return False

        return (self.bstValidator((TreeNode(-math.inf), root.left, root)) and
        self.bstValidator((root, root.right, TreeNode(math.inf))))

        


        

def main():
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3
    solution = Solution()
    result = solution.isValidBST(node1)
    print("Actual result ", result)
    print("Expected result true")


    # node4 = TreeNode(5)
    # node5 = TreeNode(1)
    # node6 = TreeNode(4)
    # node7 = TreeNode(3)
    # node8 = TreeNode(6)

    # node4.left = node5
    # node4.right = node6
    # node6.left = node7
    # node6.right = node8

    # result1 = solution.isValidBST(node4)
    # print("Actual result ", result1)
    # print("Expected result false")


    # node10 = TreeNode(1)
    # node11 = TreeNode(1)
    # node10.right = node11
    # result = solution.isValidBST(node10)
    # print("Actual result: ", result)
    # print("Expected result false")

    # node12 = TreeNode(2)
    # node12.right = TreeNode(2)
    # node12.left = TreeNode(2)
    # result = solution.isValidBST(node10)
    # print("Actual result: ", result)
    # print("Expected result false")

    # node4 = TreeNode(5)
    # node5 = TreeNode(4)
    # node6 = TreeNode(6)
    # node7 = TreeNode(3)
    # node8 = TreeNode(7)

    # node4.left = node5
    # node4.right = node6
    # node6.left = node7
    # node6.right = node8

    # result1 = solution.isValidBST(node4)
    # print("Actual result ", result1)
    # print("Expected result false")


    node20 = TreeNode(8)
    node21 = TreeNode(4)
    node22 = TreeNode(20)
    node23 = TreeNode(3)
    node24 = TreeNode(6)
    node25 = TreeNode(15)
    node26 = TreeNode(30)
    node27 = TreeNode(2)
    node28 = TreeNode(5)
    node29 = TreeNode(8)
    node30 = TreeNode(14)
    node31 = TreeNode(16)
    node32 = TreeNode(29)
    node33 = TreeNode(40)
    node20.left = node21
    node20.right = node22
    node21.left = node23
    node21.right = node24
    node22.left = node25
    node22.right = node26
    node23.left = node27
    node24.left = node28
    node24.right = node29
    node25.left = node30
    node25.right = node31
    node25.left = node32
    node25.right = node33

    result1 = solution.isValidBST(node20)
    print("Actual result ", result1)
    print("Expected result false")




if __name__=="__main__":
    main()