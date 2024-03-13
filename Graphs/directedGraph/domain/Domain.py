class DirectedGraph(object):
    def __init__(self):
        #the in edges
        self.__inEdges = {} 
        #the out edges
        self.__outEdges = {}
        #the edges with their associated cost
        self.__costs = {}
        #the number of vertices
        self.__vertices = 0
        #the number of edges
        self.__edges = 0
    
    def get_vertices(self):
        return self.__vertices
    
    def get_edges(self):
        return self.__edges
    
    def set_vertices(self, value):
        self.__vertices = value
        
    def set_edges(self, value):
        self.__edges = value 

    def get_in_edges(self):
        return self.__inEdges

    def get_out_edges(self):
        return self.__outEdges

    def get_costs(self):
        return self.__costs

    def set_in_edges(self, value):
        self.__inEdges.update(value)
        
    def append_to_key_in(self, key, value):
        self.__inEdges[key].append(value)
        
    def append_to_key_out(self, key, value):
        self.__outEdges[key].append(value)
        
    def append_costs(self, dict):
        self.__costs.update(dict)

    def set_out_edges(self, value):
        self.__outEdges.update(value)

    def set_costs(self, key, value):
        self.__costs[key] = value

    inEdges = property(get_in_edges, set_in_edges, None, None)
    outEdges = property(get_out_edges, set_out_edges, None, None)
    costs = property(get_costs, set_costs, None, None)
        
    
class RootedTree(object):
    def __init__(self, root):
        self.root = root
        self.parent = {}
        self.children = {}
        self.parent[root] = None
        self.children[root] = []
        
        
    def addChild(self, parent, child):
        self.children[child] = []
        self.parent[child] = parent
        self.children[parent].append(child)
        
    def getRoot(self):
        return self.root
        
    def getParent(self, vertex):
        return self.parent[vertex]
        
    def getChildren(self, vertex):
        return list(self.children[vertex])
        
    def isVertex(self, vertex):
        return vertex in self.parent
    
    
    



