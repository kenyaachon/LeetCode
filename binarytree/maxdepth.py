# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left)+ 1, self.maxDepth(root.right) +1)


root = TreeNode('a')
root.left = TreeNode('b')
root.left.left = TreeNode('d')
root.right = TreeNode('c')

answer = Solution()
print(answer.maxDepth(root))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(answer.maxDepth(root))

root = TreeNode(1)
root.right = TreeNode(2)
print(answer.maxDepth(root))

