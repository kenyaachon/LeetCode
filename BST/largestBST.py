
import math


class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def bstValidator(root, min, max):
    if root is None:
        return True

    if root.key < min or root.key > max:
        return False

    return bstValidator(root.left, min, root.key - 1) and bstValidator(root.right, root.key + 1, max)

def size(root) -> int:
    if root is None:
        return 0

    return size(root.left) + size(root.right) + 1

def isBST(root):
    return bstValidator(root, -math.inf, math.inf)


def largest_bst_subtree(root):
  # Fill this in.
  if root is None:
      # return 0
      return None

  if isBST(root):
      # return size(root)
      return root

  # return max(largest_bst_subtree(root.left), largest_bst_subtree(root.right))
  leftSize = size(largest_bst_subtree(root.left))
  rightSize = size(largest_bst_subtree(root.right))
  if leftSize > rightSize:
    return root.left
  return root.right



#     5
#    / \
#   6   7
#  /   / \
# 2   4   9

node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)

print ("Expected size, 3")
print ("Actual size", largest_bst_subtree(node))

node2 = TreeNode(50)
node2.left     = TreeNode(10)
node2.right     = TreeNode(60)
node2.left.left = TreeNode(5)
node2.left.right = TreeNode(20)
node2.right.left = TreeNode(55)
node2.right.left.left = TreeNode(45)
node2.right.right = TreeNode(70)
node2.right.right.left = TreeNode(65)
node2.right.right.right = TreeNode(80)
print ("Expect size is 6")
print ("Actual size", largest_bst_subtree(node2))