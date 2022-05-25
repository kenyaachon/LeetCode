
from collections import deque
from curses import intrflush
import math
import time


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


## attempt at traversing the subtree with a queue
## but it doesn't always work
def subtree54(root):
  result = ''
  que = deque()
  que.append(root)
  while len(que):
    node = que.popleft()
    result += str(node.key)
    if node.left:
      if node.left.key > node.key - 1:
        break
      que.append(node.left)

    if node.right:
      if node.right.key < node.key:
        break
      que.append(node.right)

  return result



def subtree(root):
  result = ''
  stack = []
  current = root
  while True:
    if current:
      stack.append(current)
      current = current.left
    elif (stack):
      current = stack.pop()
      if len(result):
        if int(result[-1]) > current.key:
          return result
      result += str(current.key)
      current = current.right
    else:
      break
  
  return result

  
def size(root) -> int:
    if root is None:
        return 0

    return size(root.left) + size(root.right) + 1

def subString(root) -> int:
    if root is None:
      return ""
    return str(root.key) + str(subString(root.left)) + str(subString(root.right))

def isBST(root):
    return bstValidator(root, -math.inf, math.inf)


def largest_bst_subtree_inefficient(root):
  if root is None:
      # return 0
      return None

  if isBST(root):
      # return size(root)
      return root

  # return max(largest_bst_subtree(root.left), largest_bst_subtree(root.right))
  leftSize = size(largest_bst_subtree_inefficient(root.left))
  rightSize = size(largest_bst_subtree_inefficient(root.right))
  if leftSize > rightSize:
    return root.left
  return root.right


# possible solution is 0(n^2) versus the inefficient algorithm
# the inefficient algorithm is O(2^n)
# the trade off is using a queue
# 
def largest_bst_subtree(root):
  if root is None:
    return None

  que = deque()
  que.append(root)
  largest_subtree = ""
  while len(que):
    node = que.popleft()
    result = subtree(node)
    if len(result) > len(largest_subtree):
      largest_subtree = result
    if node.left:
      que.append(node.left)
    if node.right:
      que.append(node.right)



  return largest_subtree




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
start = time.time()
print ("Actual size", largest_bst_subtree(node))
end = time.time()
print("Execution time", end-start)


# node2 = TreeNode(50)
# node2.left     = TreeNode(10)
# node2.right     = TreeNode(60)
# node2.left.left = TreeNode(5)
# node2.left.right = TreeNode(20)
# node2.right.left = TreeNode(55)
# node2.right.left.left = TreeNode(45)
# node2.right.right = TreeNode(70)
# node2.right.right.left = TreeNode(65)
# node2.right.right.right = TreeNode(80)
# print ("Expect size is 6")
# start = time.time()
# print ("Actual size", largest_bst_subtree(node2))
# end = time.time()
# print("Execution time", end-start)