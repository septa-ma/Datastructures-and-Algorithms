# what is graph?
# a non-linear data structure consisting of a set of objects where some pairs of 
# objects are connected by links, objects are represented as vertices or nodes and the 
# links that connect the vertices are called edges. 
# there are two ways to store a graph:
# 1- Adjacency Matrix
# store the graph in the 2D matrix where rows and columns denote vertices. each 
# entry in the matrix represents the weight of the edge between those vertices.
# 2- Adjacency List
# there is an array of pointer which points to the edges connected to that vertex.
# 3- dictionary
# in python and other languages which have dictionary data structure can use it.
# usage of graphs:
# - maps can be represented using graphs and then can be used by computers to 
# provide various services like the shortest path between two cities.
# - when various tasks depend on each other then this situation can be represented 
# using a Directed Acyclic graph and we can find the order in which tasks can be 
# performed using topological sort.
# - state transition diagram represents what can be the legal moves from current 
# states.

# display graph vertices
class Graph:
    def __init__(self, myGraph):
        self.myGraph = myGraph

    # show all vertiecs of a graph
    def getNodes(self):
        return list(self.myGraph.keys())

    # show all edges of a graph
    def getEdges(self):
        edgesList = []
        # find edge in graph
        for node in self.myGraph:
            for edge in self.myGraph[node]:
                if {node, edge} not in edgesList:
                    edgesList.append({node, edge})
        return edgesList

    # adding a node
    def addNode(self, newNode):
        if newNode not in self.myGraph:
            self.myGraph[newNode] = []

    # adding edges
    def addEdge(self, edge):
        for node1, node2 in edge:
            if node1 not in self.myGraph:
                self.myGraph[node1] = [node2]
            else:
                self.myGraph[node1].append(node2)
        return True
                  
    # what is DFS?
    # a traversal technique which
    # traverse each node of the graph exactly 
    # once by starting from any single node.
    # for each selected node we first print 
    # the node and then we move to one of its 
    # neighbors and print it and move to one 
    # of its neighbors and so on.
    def DFSRecursivly(self, data, visitedNodes):
        # add data in the visitedNodes
        visitedNodes.append(data)
        print(data, end=" ")
        # check all the node's neighbours recursivly
        # to find that it's visited or not
        for neighbour in self.myGraph[data]:
            if neighbour not in visitedNodes:
                self.DFSRecursivly(neighbour, visitedNodes)

    # impelemnt DFS with stack data structure
    def DFSStack(self, data):
        stack = []
        visitedNodes = []
        stack.append(data)
        visitedNodes.append(data)
        while stack:
            node = stack.pop()
            print(node, end=" ")
            # print("processing node {}.".format(node))
            for neighbour in self.myGraph[node]:
                if neighbour not in visitedNodes:
                    # print("at {}, adding {} to sack".format(node, neighbour))
                    stack.append(neighbour)
                    visitedNodes.append(neighbour)
            # print("visited nodes are:", visitedNodes)

    # what is BFS? 
    # it starts at the tree’s root or graph and visits 
    # all nodes at the current depth level before moving 
    # on to the nodes at the next depth level. 
    # using queue for implementation.
    def BFSQueue(self, data):
        queue = []
        visitedNodes = []
        queue.append(data)
        visitedNodes.append(data)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            # print("processing node {}.".format(node))
            for neighbour in self.myGraph[node]:
                if neighbour not in visitedNodes:
                    # print("at {}, adding {} to queue".format(node, neighbour))
                    queue.append(neighbour)
                    visitedNodes.append(neighbour)
            # print("visited nodes are:", visitedNodes)

# create a graph
myGraph = {
    "a" : ["b","c"],
    "b" : ["a","d"],
    "c" : ["a","d"],
    "d" : ["c","b","e"],
    "e" : ["d"]
}
graph = Graph(myGraph)
print("the graph's nodes are: ", graph.getNodes())
print("the graph's edges are: ", graph.getEdges())
graph.addNode("f")
print("the graph's nodes are: ", graph.getNodes())
edges = [['a','s'], ['l', 'h'], ['f', 'e'], ['s', 'e']]
print(graph.addEdge(edges))
print("the graph's nodes are: ", graph.getNodes())
print("the graph's edges are: ", graph.getEdges())
vl = []
print("the graph DFS recursivly: ")
graph.DFSRecursivly('a', vl)
print("\nthe graph DFS using stack: ")
graph.DFSStack('a')
print("\nthe graph BFS using queue: ")
graph.BFSQueue('a')
print()