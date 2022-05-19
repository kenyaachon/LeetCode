"""
A unival tree is a tree where all the nodes
have the same value

Given a binary tree return the unival subtree 


following example should return 5

ok a tree is unival if all the values in it are the same 

    0
1       0
    1       0
  1     1


so we can count all leaf nodes as a unival tree

if a tree has both, the root and the left child and right child 
then that is tree

??Maybe one question I do have is what about if you have a big tree

        0
    1       0

        1      0 

    1     1  
1    1    1   1

how many trees would we have in this case

"""

from ast import Pass, increment_lineno
from pickle import NONE


class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
  # Fill this in.
  
  def dfs(root):
      if root is None:
          return 0
      if root.left is None and root.right is None:
          return 1
       
    
      print("root", root.val)


      if root.left and root.right:
          if root.val == root.left.val and root.val == root.right.val:
              return dfs(root.left) + dfs(root.right) + 1
      elif root.left:
          if root.val == root.left.val:
              return dfs(root.left) + 1
      elif root.right:
          if root.val == root.right.val:
              return dfs(root.right) + 1
      
      return dfs(root.left) + dfs(root.right)


  return dfs(root)

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

b = Node(0)
b.left = Node(1)
b.right = Node(0)
b.left.left = Node(1)
b.left.right = Node(1)
b.left.left.left = Node(0)
b.left.left.right = Node(0)
b.left.right.left = Node(3)
b.left.right.right = Node(4)

b.right.left = Node(1)
b.right.left.left = Node(1)
b.right.right = Node(1)
b.right.right.right = Node(1)


print ("Actual value", count_unival_subtrees(a))
print("Expecting value 5")
# 5

print ("Actual value", count_unival_subtrees(b))
print("Expecting value 9")