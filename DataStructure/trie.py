# what is trie?
# a fast and efficient way for dynamic spell checking.
# it is also used for locating specific keys from within a set.  
# trie is like hash-table but with more advantage:
# 1- do prefix search (or auto-complete) with trie.
# 2- print all words in alphabetical order which is not easily possible with hashing.
# 3- there is no overhead of hash functions in a trie data structure.
# 4- searching for a string even in the bad case in a trie can be done in O(L).
# (L is the number of words in the query string)
# Properties:
# 1- there is one root node in each trie.
# 2- each node of a trie represents a string and each edge represents a character.
# 3- every node consists of hashmaps or an array of pointers, with each index 
# representing a character and a flag to indicate if any string ends at the current node.
# 4- contain any number of characters including alphabets, numbers, and special characters.
# 5- each path from the root to any node represents a word or string.
# using _ in for loop is because, value isn't important and the loop is just repeated n times.

# a node in the trie structure
class TrieNode:
    def __init__(self, char):
        # a dict of child nodes (keys = characters, values = nodes)
        self.children = {} 
        # the character stored in this node
        self.char = char
        # a flag for checking the end of a word 
        self.end = False

class Trie:
    def __init__(self, root):
        # the root node does not store any character
        self.root = root

    def insertion(self, word):
        # save current position
        currentNode = self.root 
        # first move down the Trie from the root
        for w in word:
            # check if the list of children has that character. 
            if w in currentNode.children:
                currentNode = currentNode.children[w]
            # if not present need to make a new TrieNode with that 
            # character and add it to the list of children.
            else:
                newNode = TrieNode(w)
                currentNode.children[w] = newNode
                currentNode = newNode
        # set end-flag to true for the last char's node of the word.
        currentNode.end = True

    def search(self, root, word):
        # save current position
        currentNode = root 
        result = ""
        # first move down the Trie from the root
        for w in word:
            # check if the list of children has that character. 
            if w in currentNode.children:
                currentNode = currentNode.children[w]
                result = ''.join([result, currentNode.char])
            else:
                result = ''.join([result, currentNode.char])
                return None, result
        return True, result


root = TrieNode("*")
trie = Trie(root)
trie.insertion("hello")
trie.insertion("hero")
trie.insertion("omit")
print(trie.search(root, "omit"))
print(trie.search(root, "omiit"))
print(trie.search(root, "hi"))
print(trie.search(root, "cake"))
print(trie.search(root, "hero"))