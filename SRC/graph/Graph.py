from SRC.tagged.storage.MapOfTaggedObjects import MapOfTaggedObjects

class Graph(object):
    START_VERTEX_NUM = 0

    def __init__(self, theVerticesStorage):
        # theVerticesStorage is TaggedObjectStorage
        self.myVertices = theVerticesStorage
        self.numEdge = 0
        self.nextFreeTag = Graph.START_VERTEX_NUM

        theObjects = theVerticesStorage.getComponents()
        for theObject in theObjects:
            if theObject.getTag() > self.nextFreeTag:
                self.nextFreeTag = theObject.getTag() + 1
        theVerticesStorage.clearAll()


    def addVertex(self, vertex, checkAdjacency=True):
        # check the vertex and its adjacency list
        # 略
        self.myVertices.addComponent(vertex)
        if vertex.getTag() >= self.nextFreeTag:
            self.nextFreeTag = self.nextFreeTag + 1
    
    def addEdge(self, vertexTag, otherVertexTag):
        # get pointers to the vertices, if one does not exist return
        vertex1 = self.getVertex(vertexTag)
        vertex2 = self.getVertex(otherVertexTag)
        if vertex1==None or vertex2==None:
            print('WARNING Graph::addEdge() - one or both of the vertices '+str(vertexTag)+' '+str(otherVertexTag)+' not in Graph.\n')
            return -1
        # add an edge to each vertex
        result = vertex1.addEdge(otherVertexTag)
        if result == 1:
            return 0 # already there
        elif result == 0: # added to vertexTag now add to other
            result=vertex2.addEdge(vertexTag)
            if result == 0:
                self.numEdge += 1
            else:
                print('WARNING Graph::addEdge() - '+str(vertexTag)+' added to '+str(otherVertexTag)+
                ' adjacency - but already there in otherVertexTag!.\n')
                return -2
        else:
            print('WARNING Graph::addEdge() - '+str(vertexTag)+' added to '+str(otherVertexTag)+
            ' adjacency - but not vica versa!.\n')
            return -2
        return result

    def getVertex(self, vertexTag):
        res = self.myVertices.getComponent(vertexTag)
        return res
    
    def getVertexs(self):
        pass
    
    def getNumVertex(self):
        pass
    
    def getNumEdge(self):
        pass
    def getFreeTag(self):
        pass
    def removeVertex(self, tag, removeEdgeFlag = True):
        pass
    
    def merge(self, other):
        pass
    
    


    
