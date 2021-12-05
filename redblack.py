"""
A red-black tree has the following properties
1. Red/Black property: Every node is colored. either red or black
2. Root property, the root is black
3. Leaf Property Every leaf (NIL) is black
4. If the a red has children, then the children are always black
5. Depth property: for each node, any simple path from this node to any of its descendant leaf
has the same black-depth
"""

"""
Algoritm to  insert a node

1. Let y be the leaf, and x be the root of the tree
2. Check if the tree is empty, 
    if it is insert newNode as a root node and color it black
3. Else
    Compare new 

"""
import sys

class Node():

    def __init__(self, item):
        self.item = item
        self.color = 1 # setting to color black
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree():

    # color - RED= 0 Black = 1
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 1 # setting to color BLACK
        self.TNULL.right = None
        self.TNULL.left = None
        self.root = self.TNULL

    def left_rotate(self, x: Node):
        print("left-rotate")
        y = x.right
        x.right = y.left

        #turn y's left subtree into x's right subtree
        if y.left != self.TNULL:
            y.left.parent = x

        #link x's parent to y
        y.parent = x.parent

        if x.parent == self.TNULL:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
             x.parent.right = y
        
        #put x on y's left
        y.left = x
        x.parent = y
        



    def right_rotate(self, x: Node):
        print("right rotate")
        y = x.left
        x.left = y.right

        #turn y's right subtree into x's right subtree
        if y.right != self.TNULL:
            y.right.parent = x

        #link x's parent to y
        y.parent = x.parent

        if x.parent == self.TNULL:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
             x.parent.left = y
        
        #put x on y's right
        y.right = x
        x.parent = y

    
    def rb_insert(self, z: Node):
        print("rb-insert")
        y = self.TNULL
        x = self.root

        while x != self.TNULL:
            y = x
            if z.item < x.item:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.TNULL:
            self.root = z
        elif z.item < y.item:
            y.left = z

        else:
            y.right = z
        
        z.left = self.TNULL
        z.right = self.TNULL
        z.color = 0 # change to color RED
        self.rb_insert_fixup(z)


    def rb_insert_fixup(self, z: Node):
        print("rb-sinert-fixup")
        while z.parent.color == 0: #color RED
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 0: #color RED
                    z.parent.color = 1 #set to color black
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 1
                    z.parent.parent.color = 0
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 0: #color RED
                    z.parent.color = 1 #set to color black
                    y.color = 1
                    z.parent.parent.color = 0
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                    z.parent.color = 1
                    z.parent.parent.color = 0
                    self.left_rotate(z.parent.parent)
        self.root.color  = 1

    def rb_transplant(self, u: Node, v: Node):
        print("rb-transplant")
        if u.parent == self.TNULL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete(self, z: Node):
        print("rb-delete")
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            #y = rb_tree_minimum(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == 1: #check if it equals black
            self.rb_delete_fixup(x)


    def rb_delete_fixup(self, x: Node):
        print("rb-delete-fixup")
        while x != self.root and x.color == 1: #check if x color is BLACk
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 0:
                    w.color = 1 
                    x.parent.color = 0 # RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.parent
                
                else:
                    if w.right.color == 1:
                        w.left.color = 1
                        w.color = 0
                        self.right_rotate(w)
                        w = x.parent.right
                    
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.right.color = 1
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 0:
                    w.color = 1 
                    x.parent.color = 0 # RED
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.parent
                
                else:
                    if w.left.color == 1:
                        w.right.color = 1
                        w.color = 0
                        self.left_rotate(w)
                        w = x.parent.left
                    
                    w.color = x.parent.color
                    x.parent.color = 1
                    w.left.color = 1
                    self.right_rotate(x.parent)
                    x = self.root
                
        x.color = 1 # BLACK


    def rb_tree_minimum(self, x: Node):
        while x.left != self.TNULL:
            x = x.left
        
        return x

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    



def main():
    bst = RedBlackTree()

    bst.rb_insert(55)
    bst.rb_insert(55)
    bst.rb_insert(55)
    bst.rb_insert(55)
    bst.rb_insert(55)
    bst.rb_insert(55)







if __name__=="__main__":
    main()

"""

A red-black tree is a binary tree that satisfies the following red-black properties
1. Every node is either red or black
2. The root is black
3. Every leaf is black
4. If a node is red, then boths its children are black
5. For each node, all simple paths from the node to descendant leaves contain the same the number
of black nodes

We call the number of black nodes on any simply path from, but not including, a node x down to a leaf the 
black-height of the node, denoted by bh(x)

A red-black tree with n internal nodes has a height at >= 2log(n + 1)
We know that the subtree rooted at any node x contains at least 2^hb(x) - 1 internal nnodes
So since we know that  each child has a black-height of either bh(x) or bh(x) - 1

So we can conclude that the child of x has 2^bh(x)- 1 -1 internal nodes

According to proerty 4, we know at least half the nodes on any simple path from the root to a leaf, not including the root, must be black
thus the black-height of the root must be at least h/2


"""