import numpy as np
import gl as gl


class Interpolation:
    def __init__(self,numOfNodes,numOfQuads):
        self.__nNodes = numOfNodes
        self.__nQuads = numOfQuads
        self.__xnodes = gl.lglnodes(self.__nNodes-1)
        self.__xquads = gl.lglnodes(self.__nQuads-1)
        self.__W      = np.diag(self.__xquads[1])
        self.__G, self.__D = gl.lagint(self.__xnodes[0],self.__xquads[0]) 

    # Returns location of nodes and quads
    def Nodes(self):
        return self.__xnodes[0]
    def Quads(self):
        return self.__xquads[0]

    # Return number of nodes and quads
    def Nn(self):
        return self.__nNodes
    def Nq(self):
        return self.__nQuads

    # Returns the interpolation matrices
    def G(self):
        return self.__G
    def D(self):
        return self.__D
    def W(self):
        return self.__W

    