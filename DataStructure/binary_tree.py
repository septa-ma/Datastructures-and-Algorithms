# what is tree?
# a non-linear and hierarchical data structure which has no loop.

# A- properties of a tree:
# 1- edges -> the connection between two nodes. a tree with N nodes has (N-1) edges.
# 2- node's depth -> the length or the number of edges of the path from the root to that node. 
# 3- node's height -> the length of the longest path from the node to a leaf node.
# 4- tree's height -> the length of the longest path from the root of the tree to a leaf.
# 5- node's degree -> the total count of subtrees attached to that node.

# B- terminologies in tree data structure:
# 1- parent node -> starter or predecessor of a node.
# 2- child node -> immediate substitute or successor of a node.
# 3- root node -> the supper node of a tree or the node which does not have any parent.
# 4- leaf node -> the nodes which do not have any child nodes.
# 5- node'sancestor -> any predecessor nodes on the path of the root to that node.
# 6- node's descendant -> any successor node on the path from the leaf node to that node.
# 7- node's sibling -> children of the same parent node are called siblings.
# 8- node's level -> the count of edges on the path from the root to that node.
# 9- internal node -> a node with at least one child is called internal node.
# 10- node's neighbour -> parent or child nodes of that node are called neighbors.
# 11- subtree -> any node of the tree along with its descendant.

# C- there are tones of tree data structures:
# 1- general tree -> a parent node can have any number of child nodes.
# 2- binary tree -> a node can have a maximum of two child nodes.
# 3- balanced tree -> the height of the left sub-tree and the right 
# sub-tree must be equal or differs at most by one. 
# 4- binary search tree -> the value of the left node is less than its parent, 
# while the value of the right node is greater than its parent.

# D- why do we need to use tree data structure?
# 1- want to store information that naturally forms a hierarchy.
# like the file system on a computer.
# 2- an ordered tree such as BST provides moderate search (quicker than linked list and slower than arrays).
# 3- trees provide moderate insertion/deletion (quicker than arrays and 
# slower than unordered linked lists).
# 4- as the same of linked lists and unlike arrays, trees don’t have an upper limit 
# on the number of nodes as nodes are linked using pointers.

# E- tree traversal algorithms:
# a process to visit all the nodes of a tree and may print their values too.
# - depth first traversal (DFS): in-order, pre-order, post-order
# - breadth first traversal (BFS): level order traversal of a tree

# binary tree:
class BinaryTree:
    count = 0
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        BinaryTree.count += 1

    # add right child
    def addRight(self, newValue):
        if self.right is None:
            self.right = BinaryTree(newValue)
        else:
            node = BinaryTree(newValue)
            node.right = self.right
            self.right = node
    
    # add left child
    def addLeft(self, newValue):
        if self.left is None:
            self.left = BinaryTree(newValue)
        else:
            node = BinaryTree(newValue)
            node.left = self.left
            self.left = node

    # showing the tree
    def showTree(self):
        if self.left:
            self.left.showTree()
        print(self.value)
        if self.right:
            self.right.showTree()

    # first the root node is visited 
    # then it’s child nodes
    # using queue for implementing
    def levelOrder(self, root):
        if root:
            # make an empty queue and enqueue the root
            queue = list()
            queue.append(root)
            while len(queue) > 0:
                # first print the first node's value of the queue
                # remove it and make it as a current node for moving
                # through the tree
                print(queue[0].value, end=" ")
                currentNode = queue.pop(0)
                # check the left-child and enqueue it
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                # check the right-child and enqueue it
                if currentNode.right is not None:
                    queue.append(currentNode.right)

    # the left subtree is visited first, 
    # then the root and later the right sub-tree. 
    # Left -> Root -> Right
    def inOrder(self, root):
        res = list()
        if root:
            res = self.inOrder(root.left)
            res.append(root.value)
            res = res + self.inOrder(root.right)
        return res

    # the root node is visited first, 
    # then the left subtree and finally the right subtree. 
    # Root -> Left -> Right
    def preOrder(self, root):
        res = list()
        if root:
            res.append(root.value)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res
    
    # first, we traverse the left subtree, 
    # then the right subtree and finally the root node.
    # Left -> Right -> Root
    def postOrder(self, root):
        res = list()
        if root:
            res = self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.value)
        return res

    #  check size of a tree
    def getSize(self):
        return BinaryTree.count

    # check if a node is leaf or not
    def isLeaf(self, root):
        if root:
            if not root.left and not root.right:
                return True, root.value
            else:
                return False, root.value
    
    # get all leaves
    def allLeaves(self, root):
        count = 0
        if root.left is None and root.right is None:
            count += 1
        if root.left:
            count += self.allLeaves(root.left)
        if root.right:
            count += self.allLeaves(root.right)
        return count

    def heightTree(self, root):
        pass


# testing binary tree:
root = BinaryTree(10)
root.addLeft(2)
root.addRight(50)
root.left.addRight(4)
root.left.addLeft(1)
root.left.left.addLeft(0)
root.left.left.addRight(3)
root.right.addLeft(30)
root.right.addRight(60)
print("levelOrder is:", end=" ")
root.levelOrder(root)
print("\ninOrder is:", root.inOrder(root))
print("preOrder is:", root.preOrder(root))
print("postOrder is:", root.postOrder(root))
print("the size of tree is:", root.getSize())
print(list(root.isLeaf(root.right.left)))
print(list(root.isLeaf(root.right.right)))
print("all the leaves of tree are:", root.allLeaves(root))

# testing binary tree:
# root = BinaryTree(10)
# root.left = BinaryTree(2)
# root.right = BinaryTree(30)
# root.left.right = BinarootryTree(4)
# root.right.right = BinaryTree(50)
# print("inorder: ",root.inorder(root))
# print("preorder: ",root.preorder(root))
# print("postorder: ",root.postorder(root))
# print(root.value, root.left.value, root.right.value, root.left.right.value, root.right.right.value)