

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        #swap the elements
        temp = root.left
        root.left = root.right
        root.right = temp

        #traverse the tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        



    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printCurrentLevel(root, i)
 
 
    # Print nodes at a current level
    def printCurrentLevel(self, root , level):
        if root is None:
            return
        if level == 1:
            print(root.val,end=" ")
        elif level > 1 :
            self.printCurrentLevel(root.left , level-1)
            self.printCurrentLevel(root.right , level-1)

    """ Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """
    def height(self, node):
        if node is None:
            return 0
        else :
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
    
            #Use the larger one
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1



def main():
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    answer = Solution()
    result = answer.invertTree(node1)
    print("\nprevious answer 4, 2, 7, 1, 3, 6, 9")
    answer.printLevelOrder(result)


    node11 = TreeNode(2)
    node11.left = TreeNode(1)
    node11.right = TreeNode(3)
    print("\nprevious answer: 2, 3, 1")
    result = answer.invertTree(node11)
    answer.printLevelOrder(result)

    print("\nprevious answer [] ")
    result = answer.invertTree(None)
    answer.printLevelOrder(result)

    node12 = TreeNode(4)
    node13 = TreeNode(2)
    node14 = TreeNode(7)
    node15 = TreeNode(1)
    node16 = TreeNode(3)
    node12.left = node13
    node12.right = node14
    node13.left = node15
    node13.right = node16
    print("\nprevious answer 4, 2, 7, 1, 3")
    result = answer.invertTree(node12)
    answer.printLevelOrder(result)

if __name__=="__main__":
    main()
