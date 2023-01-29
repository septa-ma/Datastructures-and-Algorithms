# binary tree and binary search tree:
class BST:
    count = 0
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        BST.count += 1
 
    # 1- adding a new node in a BST
    # if tree hasn't a root node insert it as a root.
    # if node's value is less than the root's value insert it in the left-side.
    # otherwise it's bigger than the root insert it in the right-side.
    def insert(self, newValue):
        if self.value:
            if self.value < newValue:
                if self.right is None:
                    self.right = BST(newValue)
                else:
                    self.right.insert(newValue)
            elif self.value > newValue:
                if self.left is None:
                    self.left = BST(newValue)
                else:
                    self.left.insert(newValue)
            else:
                return False
        else:
            self.value = newValue

    # 2- finding a node in a BST
    # if node's value is less than root search in the left-side.
    # otherwise it's bigger than root search in the right-side.
    def search(self, root, data):
        try:
            if root.value == data:
                return True
            elif data < root.value:
                return self.search(root.left, data)
            elif data > root.value:
                return self.search(root.right, data)
        except AttributeError:
            return False

    # 3- removeing a node in a BST
    # 1- if no children is a leaf -> just delete.
    # 2- if a single child -> copy that child to the node.
    # 3- if two children -> determine the next highest element (inorder successor)
    # the maximum node in left subtree or minimum node in right subtree
    def remove(self, root, data):
        # chaeck if have a tree
        if root is None:
            return root
        # find the node to be removed
        if data < root.value:
            root.left = self.remove(root.left, data)
        elif(data > root.value):
            root.right = self.remove(root.right, data)
        else:
            # node with no child or one
            if root.left is None:
                BST.count -= 1
                return root.right
            elif root.right is None:
                BST.count -= 1
                return root.left
            # node with tow children
            # find the min-value in right subtree
            # put the min-value instead af del-value
            # remove the duplicate node
            minValue = self.minRightSubtree(root.right)
            root.value = minValue
            root.right = self.remove(root.right, root.value)
            
        return root

    # 5- finding the minimum value in right child of the node.
    def minRightSubtree(self, rightRoot):
        currentNode = rightRoot
        while currentNode and currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

    # the left subtree is visited first, 
    # then the root and later the right sub-tree. 
    # Left -> Root -> Right
    def inorder(self, root):
        res = list()
        if root:
            res = self.inorder(root.left)
            res.append(root.value)
            res = res + self.inorder(root.right)
        return res

    def size(self):
        return BST.count

    def isLeaf(self, root):
        for i in range(0, self.size()):
            if self is None or root.right is None:
                return root.value, True
            else:
                return root.value, False


# testing binary search tree:
root = BST(14)
root.insert(25)
root.insert(10)
root.insert(20)
root.insert(2)
root.insert(30)
root.insert(8)
root.insert(5)
root.insert(40)
root.insert(11)
root.insert(13)
print(root.search(root, 24))
print("leaf node:",root.isLeaf(root.right.right.right))
print("leaf node:",root.isLeaf(root.right.right))
print("the size of tree is %i " %(root.size()))
print("inorder:",root.inorder(root))
root.remove(root, 10)
root.remove(root, 30)
root.remove(root, 11)
root.remove(root, 8)
root.remove(root, 2)
print("the size of tree is %i " %(root.size()))
print("inorder:",root.inorder(root))
