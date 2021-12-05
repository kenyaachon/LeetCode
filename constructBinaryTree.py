#Definition for a binary tree node.
from typing import List, Set
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addNodeLeft(self, value: int, root: TreeNode):

        print("Add Node Left")

    def addNodeRemain(self, value: int, root: TreeNode, height: int):
        print("Add Node Right")
        print("root", root.val)
        if root == None:
            return
        if root.left != None and root.right != None:
            node = TreeNode(value)
            root.left = node
        count = 0
        pred = None
        while root.left:
            print("root.left")
            if count < height - 1:
                print("count", count)
                pred = root
                root = root.left
                print("count root", root.val)
                count += 1
            elif count == height - 1:
                print("put right", value)
                print("put right count", root.val)
                print("count", count)
                if root.left == None:
                    root.left = TreeNode(value)
                elif root.right == None:
                    root.right = TreeNode(value)
                    break
                elif root:
                    root = root.left
                else:
                    height -= 1
                    count -= 1
                    root = pred

                


        
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) == 2:
            node1 = TreeNode[preorder[0]]
            node2 = TreeNode[preorder[1]]
            node1.left = node2
            return node1
        preOrderpos = 0
        inOrderpos = 0

        root = TreeNode(preorder[preOrderpos])
        rootCopy = root
        preOrderSet = set()
        preOrderSet.add(preorder[preOrderpos])
        #rootCopy = root
        preOrderpos += 1
        height = 0
        #predecessor = None
        while preOrderpos < len(preorder) and inOrderpos < len(inorder):
            while preOrderpos < len(preorder):

                if preorder[preOrderpos] == inorder[inOrderpos]:
                    print("last left")
                    root.left = TreeNode(preorder[preOrderpos])
                    preOrderSet.add(preorder[preOrderpos])
                    height += 1
                    #predecessor = root
                    break
                print("left node")
                root.left = TreeNode(preorder[preOrderpos])
                preOrderSet.add(preorder[preOrderpos])
                height += 1
                #predecessor = root
                root = root.left
                preOrderpos += 1

        
            
            while preOrderpos < len(preorder) and inOrderpos < len(inorder):
                print("trying to find preorder  inorder", preorder[preOrderpos], inorder[inOrderpos] )
                if preorder[preOrderpos] == inorder[inOrderpos]:
                    inOrderpos += 1
                    if inOrderpos < len(inorder):
                        if inorder[inOrderpos] in preOrderSet:
                            print("adding a right")
                            preOrderpos += 1
                            print("adding a right", preorder[preOrderpos])
                            self.addNodeRemain(preorder[preOrderpos], rootCopy, height)
                            preOrderSet.add(preorder[preOrderpos])
                            inOrderpos += 1
                        else:
                            print("add a couch right", preorder[preOrderpos])
                            preOrderpos += 1
                            self.addNodeRemain(preorder[preOrderpos], rootCopy, height)
                            preOrderSet.add(preorder[preOrderpos])
                else:
                    if preorder[preOrderpos + 1] == inorder[inOrderpos]:
                        preOrderpos += 1
                        print("adding a right else", preorder[preOrderpos])
                        self.addNodeRemain(preorder[preOrderpos], rootCopy, height)
                        preOrderSet.add(preorder[preOrderpos])
        
        return rootCopy

    
    def createMap(self, inorder: List) -> dict:
        inOrderMap = {}
        for index, value in enumerate(inorder):
            inOrderMap[value] = index
        
        return inOrderMap

    #def arrayToTree(self, positions: List, inOrderMap: dict, preorder: List):
    def arrayToTree(self, positions: List, preorder: List):

        left = positions[0]
        right = positions[1]
        #preOrderpos = positions[2]

        if left > right:
            return None
        

        if self.preOrderpos < len(preorder):
            rootValue =  preorder[self.preOrderpos]
            print("left %d right %d rootValue %d", left, right, rootValue)

            root = TreeNode(rootValue)
            self.preOrderpos += 1
            positions = [left, self.inOrderMap[rootValue] - 1]
            #root.left = self.arrayToTree(positions, inOrderMap, preorder)
            root.left = self.arrayToTree(positions, preorder)


            positions = [self.inOrderMap[rootValue] + 1, right]
            #root.right = self.arrayToTree(positions, inOrderMap, preorder)
            root.right = self.arrayToTree(positions, preorder)

        
            return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        self.preOrderpos = 0
        self.inOrderMap = self.createMap(inorder)

        positions = [0, len(preorder) - 1]
        return self.arrayToTree(positions, preorder)
        #return TreeNode()

def preOrderPrint(root: TreeNode):
    if root == None:
        return
    
    print(root.val)
    preOrderPrint(root.left)
    preOrderPrint(root.right)

def main():

    """
    preorderInput = [1,2,4,5,3]
    inorderInput = [4,2,5,1,3]
    result = Solution()
    root = result.buildTree(preorderInput, inorderInput)
    preOrderPrint(root)
    """
    
    preorderInput = [3,9,20,15,7]
    inorderInput = [9,3,15,20,7]
    result = Solution()
    root = result.buildTree(preorderInput, inorderInput)
    preOrderPrint(root)    


    """
    inorderInput =  [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90]
    preorderInput = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90]
    result = Solution()
    root = result.buildTree(preorderInput, inorderInput)
    preOrderPrint(root)
    """
    

if __name__=="__main__":
    main()

