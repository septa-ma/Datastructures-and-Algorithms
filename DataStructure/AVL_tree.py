# what is AVL tree?
# a self-balancing Binary Search Tree (BST) where the difference between heights
# of left and right subtrees for every node are less than or equal to 1.
# balance-factor = hight_left_subtree - hight_right_subtree = {-1,0,1}.
# why we use AVL tree?
# in BST time complexity in bad-case is O(n) and in best-case is O(logn).
# if we want to have a search in BST with best-case time complexity, we must 
# to use rotation to convert a BST into a AVL tree and balance it.
# T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) 
# or x (on the right side)     
      
#      y                               x
#     / \     Right Rotation          /  \
#    x   T3   - - - - - - - >        T1   y 
#   / \       < - - - - - - -            / \
#  T1  T2     Left Rotation            T2  T3

# keys in both of the above trees follow the following order 
# keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
# so BST property is not violated anywhere.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    
    # calculate height of each sub-tree
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    # check if the tree is balance or not
    def isBalance(self, node):
        if node is None:
            return 0 
        return self.getHeight(node.left) - self.getHeight(node.right)

    # if balance-factor is a positive number do this rotation
    # 1- tempNewRoot -> right child of unblanced root 
    # 2- tempLeftSub -> left child of tempNewRoot
    # 3- rotate the tree, unblanced root become left child of tempNewRoot
    # 4- tempLeftSub become right child of unblanced root
    # 5- updates heights of unbalanced and new root
    def leftRotation(self, node):
        tempNewRoot = node.right
        tempLeftSub = tempNewRoot.left
        tempNewRoot.left = node
        node.right = tempLeftSub
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        tempNewRoot.height = 1 + max(self.getHeight(tempNewRoot.left), self.getHeight(tempNewRoot.right))
        return tempNewRoot
    
    # if balance-factor is a negetive number do this rotation
    # 1- tempNewRoot -> left child of unbalanced root
    # 2- tempRightSub -> right child of tempNewRoot
    # 3- rotate the tree, unblanced root become right child of tempNewRoot
    # 4- tempLeftSub become left child of unblanced root
    # 5- updates heights of unbalanced and new root
    def rightRotation(self, node):
        tempNewRoot = node.left
        tempRightSub = tempNewRoot.right
        tempNewRoot.right = node
        node.left = tempRightSub
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        tempNewRoot.height = 1 + max(self.getHeight(tempNewRoot.left), self.getHeight(tempNewRoot.right))
        return tempNewRoot

    # insertion
    def AVLInsertion(self, root, data):
        if root is None:
            return TreeNode(data)
        elif data <= root.value:
            root.left = self.AVLInsertion(root.left, data)
        elif data > root.value:
            root.right = self.AVLInsertion(root.right, data) 
        # rotate tree
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.isBalance(root)
        return self.rotateAfterInsertion(root, balance, data)

    # there are 4 ways of rotation use one of the for each insertion.
    def rotateAfterInsertion(self, root, balance, data):
        # 1- left-left rotation -> balance is a positive number
        # and data which inserted is less than left-value root.
        # it's left-left child of root.
        if balance > 1 and data < root.left.value:
            return self.rightRotation(root)
        # 2- right-right rotation -> balance is a negetive number
        # and data which inserted is more than right-value root.
        # it's right-right child of root.
        if balance < -1 and data > root.right.value:
            return self.leftRotation(root)
        # 3- left-right rotation -> balance is a positive number
        # and data which inserted is more than left-value root.
        # it's left-right chile of root.
        if balance > 1 and data > root.left.value:
            # first make it left-left then right rotate it.
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        # 4- right-left rotation -> balance is a negetive number
        # and data which inserted is less than right-value root.
        # it's right-left child of root.
        if balance < -1 and data < root.right.value:
            # first make it right-right then left rotate it.
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
        return root
    
    # find min value in right-subtree
    def minRightSubtree(self, rightRoot):
        currentNode = rightRoot
        while currentNode and currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

    # deletion
    def AVLDeletion(self, root, data):
        # chaeck if have a tree
        if root is None:
            return root
        # find the node to be removed
        if data < root.value:
            root.left = self.AVLDeletion(root.left, data)
        elif(data > root.value):
            root.right = self.AVLDeletion(root.right, data)
        else:
            # node with no child or one
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # node with tow children
            # find the min-value in right subtree
            # put the min-value instead af del-value
            # remove the duplicate node
            minValue = self.minRightSubtree(root.right)
            root.value = minValue
            root.right = self.AVLDeletion(root.right, root.value)
        # rotate tree
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.isBalance(root)
        return self.rotateAfterdeletion(root, balance)

    # rotate tree after removeing a node
    def rotateAfterdeletion(self, root, balance):
        if balance > 1 and self.isBalance(root.left) >= 0:
            return self.rightRotation(root)
        if balance < -1 and self.isBalance(root.right) <= 0:
            return self.leftRotation(root)
        if balance > 1 and self.isBalance(root.left) < 0:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        if balance < -1 and self.isBalance(root.right) > 0:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
        return root

    def preOrder(self, root):
        res = list()
        if root:
            res.append(root.value)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res


tree = AVLTree()
tnode = None
tnode = tree.AVLInsertion(tnode, 10)
tnode = tree.AVLInsertion(tnode, 20)
tnode = tree.AVLInsertion(tnode, 30)
tnode = tree.AVLInsertion(tnode, 40)
tnode = tree.AVLInsertion(tnode, 50)
tnode = tree.AVLInsertion(tnode, 25)
print("Preorder after insertion:")
print(tree.preOrder(tnode))
tnode = tree.AVLDeletion(tnode, 50)
tnode = tree.AVLDeletion(tnode, 10)
print("Preorder after remove:")
print(tree.preOrder(tnode))
tnode = tree.AVLInsertion(tnode, 55)
tnode = tree.AVLInsertion(tnode, 15)
tnode = tree.AVLInsertion(tnode, 19)
print("Preorder after insertion:")
print(tree.preOrder(tnode))