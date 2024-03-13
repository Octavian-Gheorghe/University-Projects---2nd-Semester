from domain.Domain import DirectedGraph, RootedTree
from errors.Errors import RepoError
from random import randint

class RepoGraph(object):
    def __init__(self, __fileName):
        self.__list = DirectedGraph()
        self.__copy = DirectedGraph()
        self.__fileName = __fileName
        #self.randomGraph(1000, 10)
        self.loadFromFile()
        
    def getNumber(self):
        return self.__list.get_vertices()
    
    
    def loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            aux = line.split(" ")
            self.__list.set_vertices(aux[0])
            self.__list.set_edges(aux[1])
            line = f.readline().strip()
            while line != "":
                aux = line.split(" ")
                aux[0] = int(aux[0])
                aux[1] = int(aux[1])
                aux[2] = int(aux[2])
                if aux[0] in self.__list.get_out_edges().keys():
                    self.__list.append_to_key_out(aux[0], aux[1])
                else:
                    self.__list.set_out_edges({aux[0] : [aux[1]]})
                if aux[1] in self.__list.get_in_edges().keys():
                    self.__list.append_to_key_in(aux[1], aux[0])
                else:
                    self.__list.set_in_edges({aux[1] : [aux[0]]})
                self.__list.append_costs({(aux[0], aux[1]) : aux[2]})
                line = f.readline().strip()
                
        except IOError:
            raise RepoError()
        finally:
            f.close()
                
    def parse(self):
        for key in self.__list.get_out_edges():
            for i in range(0, len(self.__list.get_out_edges()[key])):
                print("From " + str(key) + " to " + str(self.__list.get_out_edges()[key][i]))
            
    def find(self, firstVertex, secondVertex):
        firstVertex = int(firstVertex)
        if firstVertex in self.__list.get_out_edges().keys() and int(secondVertex) in self.__list.get_out_edges()[firstVertex]:
            return True
        return False 
    
    def getDegree(self, vertex):
        inDegree = 0
        outDegree = 0
        vertex = int(vertex)
        if vertex in self.__list.get_in_edges().keys():
            inDegree = len(self.__list.get_in_edges()[vertex])
        if vertex in self.__list.get_out_edges().keys():
            outDegree = len(self.__list.get_out_edges()[vertex])
        return (inDegree, outDegree)
    
    def parseOutbound(self, vertex):
        vertex = int(vertex)
        if (vertex > int(self.__list.get_vertices())):
            print("the vertex does not exist")
        else:
            for elem in self.__list.get_out_edges()[vertex]:
                print(str(elem))
    
    def parseInbound(self, vertex):
        vertex = int(vertex)
        if (vertex > int(self.__list.get_vertices())):
            print("the vertex does not exist")
        else:
            for elem in self.__list.get_in_edges()[vertex]:
                print(str(elem))
    
    def getEnd(self, edgeId):
        pass
    
    def retrieve(self, firstVertex, secondVertex, information):
        if firstVertex not in self.__list.get_in_edges()[secondVertex]:
            print("The edge does not exist")
        else:
            firstVertex = int(firstVertex)
            secondVertex = int(secondVertex)
            information = int(information)
            edge = (firstVertex, secondVertex)
            initial = self.__list.get_costs()[edge]
            self.__list.set_costs(edge, information)
            return initial
        
    def add(self, firstVertex, secondVertex, cost):
        firstVertex = int(firstVertex)
        secondVertex = int(secondVertex)
        cost = int(cost)
        if firstVertex not in self.__list.get_in_edges()[secondVertex]:
            if firstVertex in self.__list.get_out_edges().keys():
                self.__list.append_to_key_out(firstVertex, secondVertex)
            else:
                self.__list.set_out_edges({firstVertex : [secondVertex]})
            if secondVertex in self.__list.get_in_edges().keys():
                self.__list.append_to_key_in(secondVertex, firstVertex)
            else:
                self.__list.set_in_edges({secondVertex : [firstVertex]})
            self.__list.append_costs({(firstVertex, secondVertex) : cost})
            
            if int(self.__list.get_vertices()) < int(firstVertex):
                self.__list.set_vertices(firstVertex)
            
            if int(self.__list.get_vertices()) < int(secondVertex):
                self.__list.set_vertices(secondVertex)
        else:
            print("The edge already exists")
        
    def remove(self, firstVertex, secondVertex):
        firstVertex = int(firstVertex)
        secondVertex = int(secondVertex)
        if firstVertex not in self.__list.get_in_edges()[secondVertex]:
            print("The edge does not exist")
        else:
            del self.__list.get_costs()[(firstVertex, secondVertex)]
            self.__list.get_out_edges()[firstVertex].remove(secondVertex)
            self.__list.get_in_edges()[secondVertex].remove(firstVertex)
            
    
    def addVer(self, vertex):
        vertex = int(vertex)
        value = int(self.__list.get_vertices()) + 1
        if int(self.__list.get_vertices()) < int(vertex):
            self.__list.set_vertices(vertex)
        else:
            print("Vertex already exits")
    
    def removeVer(self, vertex):
        vertex = int(vertex)
        if ( self.getDegree(vertex)[0] == 0 and self.getDegree(vertex)[1] == 0):
            print("removed vertex")
        else:
            for elem in self.__list.get_in_edges()[vertex]:
                del self.__list.get_costs()[(vertex, elem)]
                self.__list.get_in_edges()[vertex].remove(elem)
                self.__list.get_out_edges()[elem].remove(vertex)
            del self.__list.get_in_edges()[vertex]
            
            for elem in self.__list.get_out_edges()[vertex]:
                del self.__list.get_costs()[(elem, vertex)]
                self.__list.get_out_edges()[vertex].remove(elem)
                self.__list.get_in_edges()[elem].remove(vertex)
            del self.__list.get_out_edges()[vertex]
            
    def copy(self):
        self.__copy = self.__list
        for key in self.__copy.get_in_edges():
            for i in range(0, len(self.__copy.get_in_edges()[key])):
                print("From " + str(key) + " to " + str(self.__copy.get_in_edges()[key][i]))
        
        return self.__list
    
    
    def randomGraph(self, numberOfEdges, vertices):
        for i in range(numberOfEdges):
            x = randint(0, vertices)
            y = randint(0, vertices)
            w = randint(0, 300)
            if ( x == y ):
                i -= 1
            else:
                if x in self.__list.get_out_edges().keys():
                    self.__list.append_to_key_out(x, y)
                else:
                    self.__list.set_out_edges({x : [y]})
                if y in self.__list.get_in_edges().keys():
                    self.__list.append_to_key_in(y, x)
                else:
                    self.__list.set_in_edges({y : [x]})
                self.__list.append_costs({(x, y) : w})
                
    def bfs(self, startVertex):
        queue = [] 
        front = 0
        viz = {}
        viz[startVertex] = 1
        tree = RootedTree(startVertex)
        queue.append(startVertex )
        
        while front < len(queue) :
            for child in self.__list.get_in_edges()[queue[front]]:
                if child not in viz :
                    queue.append(child)
                    viz[child] = 1
                    tree.addChild(queue[front],child)
            
            front += 1
        
        return tree


    def lowestLengthPath(self, firstVertex, secondVertex):
        queue = []
        visited = []
        distance = {}
        prev = []
        path = {}
        queue.append(secondVertex)
        visited.append(secondVertex)
        distance.update({secondVertex : 0})
        aux = secondVertex
        while len(queue) > 0 :
            aux = queue.pop(0)
            if self.getDegree(aux)[0] > 0:
                for y in self.__list.get_in_edges()[aux]:
                    if y not in visited:
                        queue.append(y)
                        visited.append(y)
                        dist = distance[aux] + 1
                        path.update({y : aux})
                        distance.update({y : dist})
                        if y == firstVertex:
                            break;
                        
        if firstVertex not in distance.keys():
            print("There is no path")
        else:
            print(distance[firstVertex])
            node = firstVertex
            while node != secondVertex:
                print(node)
                node = path[node]
            print(secondVertex)
        
        return path
        
    def printTree(self, tree):
        self.printSubTree(tree, tree.getRoot(), 0)
    
    def printSubTree(self, tree, vertex, nrSpaces):
        print(" "*nrSpaces + str( vertex) )
        for v in tree.getChildren(vertex):
           self.printSubTree(tree, v, nrSpaces+1)    
    
         