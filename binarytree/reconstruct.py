from collections import deque
from tkinter.tix import Tree

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result



def reconstruct(preorder, inorder):
    #Fill this in

    stack = []
    size = len(preorder)

    if size == 1:
        return Node(preorder[0])
    
    preI = 0 #increment for preorder
    inI = 0 #increment for inOrder

    def peek(stack):
        if len(stack) == 0:
            return None
        return stack[len(stack) - 1]

    topNode = None
    topNodeVal = preorder[0]
    currentNode = None
    while (preI <= size and inI < size):

        print(stack)
        if peek(stack) == inorder[inI]:
            value = stack.pop()
            inI += 1

            # print(value)
            # TODO: ADD WAY TO ADD THE NODES to the tree
            new = Node(value)

            if len(stack) == 0:
                if value == topNodeVal:
                    new.left = currentNode
                    currentNode = new
                    topNode = new
                elif currentNode.left is None:
                    currentNode.left = new
                    temp = currentNode.val
                    currentNode.val = new.val
                    new.val = temp
                elif currentNode.left:
                    currentNode.right = new
                else:
                    print("fall through")
                
                    
            else:
                if currentNode is None:
                    currentNode = new
                elif currentNode.left:
                    currentNode.right = new
                    if topNode:
                        currentNode = currentNode.right
                elif topNode is None:
                    new.left = currentNode
                    currentNode = new
        else:
            print(preI)
            stack.append(preorder[preI])
            preI += 1


    return topNode

def printInorder(root):

    if root is None:
        return
    printInorder(root.left)

    print(root.val, " ")

    printInorder(root.right)
    

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
# print(str(Node(2)))
printInorder(tree)
# print (" Actual result ", str(tree))
print ("Expected result abcdefg")

tree = reconstruct([3,9,20,15,7], [9,3,15,20,7])
# print ("Actual result ", str(tree))
printInorder(tree)
print ("Expected result 3,9, 20, null, null, 15, 7")

