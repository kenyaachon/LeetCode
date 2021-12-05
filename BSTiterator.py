# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        # print("just getting started")
        self.__result = self.traverse(root)
        # print(self.__result)
        self.__pointer = -1

    def traverse(self, root):
        if root is None:
            return []
        
        return self.traverse(root.left) + [root.val] + self.traverse(root.right)
        

    def next(self) -> int:
        if self.__pointer == -1:
            self.__pointer = 0
        else:
            self.__pointer += 1
        
        if self.__pointer < len(self.__result):
            return self.__result[self.__pointer]
        

    def hasNext(self) -> bool:
        if self.__pointer < len(self.__result) - 1:
            return True
        return False



node1 = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(15)
node1.left = node2
node1.right = node3
node4 = TreeNode(9)
node5 = TreeNode(20)
node3.left = node4
node3.right = node5
obj = BSTIterator(node1)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())


