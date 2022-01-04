from collections import deque
from typing import List, Optional
import math

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.val)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        
        current = TreeNode(nums[0])
        root = TreeNode(nums[0])
        height = 0
        for item in nums[1:n]:
            if item > current.val:
                if current.right is None and current.left is None:
                    if height < int(math.log(n, 2)):
                        root = TreeNode(item)
                        root.left = current
                        current = root
                        height += 1
                elif current.left is not None and current.right is None:
                    current.right = TreeNode(item)
                    if height == int(math.log(n, 2)):
                        current = current.right
                else:
                    root = TreeNode(item)
                    root.left = current
                    current = root
                    height += 1
                    
            else:
                current.left = item
                current = current.left
        return root

answer = Solution()
print("expected result", "4261357" )
print("Actual result", answer.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]))
# print("Actual result", answer.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]))
