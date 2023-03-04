from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def getValues(self):
        pass

    def processValues(self):
        pass

    def showValues(self):
        pass


class NetshoesGraph(Graph):
    def getValues(self):
        pass