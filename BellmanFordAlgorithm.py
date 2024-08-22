#similar to dijksra's algorithm but it can handle negative weights on the graph

class graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    #function to add an edge
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    #to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.v):
            print("{0}\t\t{1}".format(i, dist[i]))

    #function to find the shortest path
    def BellmanFord(self, src):
        dist = [float("Inf")] * self.v #initialize
        dist[src] = 0

        for _ in range(self.v -1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w #update the distance

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
            
        self.printArr(dist)

if __name__ == '__main__':
    g = graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # function call
    g.BellmanFord(0)
