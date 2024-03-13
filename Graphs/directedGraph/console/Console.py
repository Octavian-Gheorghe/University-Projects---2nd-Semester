from controller.Controller import Controller
from errors.Errors import ValidError

class Console(object):
    def __init__(self, __controller):
        self.__controller = __controller
    
    def uiGetTheNumberOfVertices(self):
        print(self.__controller.getNumberOfVertices())
    
    def uiParseTheVertices(self):
        self.__controller.parseTheVertices()
    
    def uiFindEdge(self):
        firstVertex = input("First vertex: ")
        secondVertex = input("Second vertex: ")
        print(self.__controller.findEdge(firstVertex, secondVertex))
    
    def uiGetInDegreeOutDegree(self):
        vertex = input("Vertex: ")
        degrees = self.__controller.getInDegreeOutDegree(vertex)
        print("In degree = " + str(degrees[0]) + ", Out degree = " + str(degrees[1]))
    
    def uiParseOutboundEdges(self):
        vertex = input("Vertex: ")
        self.__controller.parseOutboundEdges(vertex)
        
    def uiParseInboundEdges(self):
        vertex = input("Vertex: ")
        self.__controller.parseInboundEdges(vertex)
    
    def uiGetEndpoints(self):
        edgeId = input("Edge Id: ")
        self.__controller.getEndpoints(edgeId)
    
    def uiRetrieveModifyInformation(self):
        firstVertex = input("First vertex of the edge: ")
        secondVertex = input("Second vertex of the edge: ")
        information = input("Information of the edge: ")
        initial = self.__controller.retrieveModifyInformation(firstVertex, secondVertex, information)
        print("Initial cost: " + str(initial))
    
    def uiAddEdge(self):
        firstVertex = input("First vertex of the edge: ")
        secondVertex = input("Second vertex of the edge: ")
        cost = input("Cost of the edge: ")
        self.__controller.addEdge(firstVertex, secondVertex, cost)
        
    def uiRemoveEdge(self):
        firstVertex = input("First vertex of the edge: ")
        secondVertex = input("Second vertex of the edge: ")
        self.__controller.removeEdge(firstVertex, secondVertex)
    
    def uiAddVertex(self):
        vertex = input("Vertex: ")
        self.__controller.addVertex(vertex)
    
    def uiRemoveVertex(self):
        vertex = input("Vertex: ")
        self.__controller.removeVertex(vertex)
    
    def uiCopyGraph(self):
        copy = self.__controller.copyGraph()
        
    def uilowestLengthPath(self):
        firstVertex = input("First vertex: ")
        secondVertex = input("Second vertex: ")
        print(str(self.__controller.shortestPath(firstVertex, secondVertex)))
    
    def printMenu(self):
        print("1. Get the number of vertices")
        print("2. Parse the set of vertices")
        print("3. Find edge")
        print("4. Get the in degree and the out degree of a specified vertex")
        print("5. Parse the set of outbound edges of a specified vertex")
        print("6. Parse the set of inbound edges of a specified vertex")
        print("7. Get the endpoints of an edge")
        print("8. Retrieve or modify the information attached to a specified edge")
        print("9. Add an edge")
        print("10. Remove an edge")
        print("11. Add a vertex")
        print("12. Remove a vertex")
        print("13. Copy the graph")
        print("14. Find the lowest path between two vertices")
        print("15. Exit")
    
    def run(self):
        commands = {"1" : self.uiGetTheNumberOfVertices, 
                    "2" : self.uiParseTheVertices, 
                    "3" : self.uiFindEdge, 
                    "4" : self.uiGetInDegreeOutDegree, 
                    "5" : self.uiParseOutboundEdges, 
                    "6" : self.uiParseInboundEdges, 
                    "7" : self.uiGetEndpoints, 
                    "8" : self.uiRetrieveModifyInformation, 
                    "9" : self.uiAddEdge, 
                    "10": self.uiRemoveEdge, 
                    "11": self.uiAddVertex, 
                    "12": self.uiRemoveVertex, 
                    "13": self.uiCopyGraph, 
                    "14": self.uilowestLengthPath}
        while True:
            try:
                self.printMenu()
                x = input("Please give a command: ")
                if x == "15":
                    return 
                if x in commands.keys():
                    commands[x]()
            except ValidError as v:
                print(v)


