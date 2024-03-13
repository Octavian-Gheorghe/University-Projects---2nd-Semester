from repo.Repository import RepoGraph

class Controller(object):
    def __init__(self, __repo):
        self.__repo = __repo
        
    def getNumberOfVertices(self):
        return self.__repo.getNumber()
        
    def parseTheVertices(self):
        return self.__repo.parse()
    
    def findEdge(self, firstVertex, secondVertex):
        return self.__repo.find(firstVertex, secondVertex);
    
    def getInDegreeOutDegree(self, vertex):
        return self.__repo.getDegree(vertex)
    
    def parseOutboundEdges(self, vertex):
        self.__repo.parseOutbound(vertex)
    
    def parseInboundEdges(self, vertex):
        self.__repo.parseInbound(vertex)
    
    def getEndpoints(self, edgeId):
        pass
    
    def retrieveModifyInformation(self, firstVertex, secondVertex, information):
        return self.__repo.retrieve(firstVertex, secondVertex, information)
    
    def addEdge(self, firstVertex, secondVertex, cost):
        self.__repo.add(firstVertex, secondVertex, cost)
    
    def removeEdge(self, firstVertex, secondVertex):
        self.__repo.remove(firstVertex, secondVertex)
    
    def addVertex(self, vertex):
        self.__repo.addVer(vertex)
    
    def removeVertex(self, vertex):
        self.__repo.removeVer(vertex)
    
    def copyGraph(self):
        return self.__repo.copy()

    def shortestPath(self, firstVertex, secondVertex):
        firstVertex = int(firstVertex)
        secondVertex = int(secondVertex)
        self.__repo.lowestLengthPath(firstVertex, secondVertex);

