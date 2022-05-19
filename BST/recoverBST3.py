class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # predecessor is a Morris predecessor. 
        # In the 'loop' cases it could be equal to the node itself predecessor == root.
        # pred is a 'true' predecessor, 
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None
        
        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:       
                # Predecessor node is one step left 
                # and then right till you can.
                print("root.left")
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    print("predecessor.right and predecessor.right != root", predecessor)
 
                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                    print("predecessor.right is None", predecessor.right)
                    print("predecessor.right root", root)
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        print("pred and root.val < pred.val", pred.val, root.val, pred.val)
                        y = root
                        if x is None:
                            x = pred 
                    pred = root
                    
                    predecessor.right = None
                    root = root.right
                    print("link is broken, time to change subtree", root)
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    print("pred and root.val < pred.val", pred.val, root.val, pred.val)
                    y = root
                    if x is None:
                        x = pred 
                pred = root
                
                root = root.right

                print("just go right", root)
        
        x.val, y.val = y.val, x.val

    def inOrderPrint(self, root: TreeNode) -> None:
        if root == None:
            print(None)
            return
        
        print(root.val)
        self.inOrderPrint(root.left)
        self.inOrderPrint(root.right)

def main():

    """
    
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node1.left = node2
    node2.right = node3
    result = Solution()
    print("Expected output [3, 1, null, null, 2]")
    result.recoverTree(node1)
    result.inOrderPrint(node1)


    """

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
    """

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

    """

    
if __name__=="__main__":
    main()