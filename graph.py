"""
Demo the implementation using the adjacency list
"""


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, name):
        if name not in self.neighbors:
            self.neighbors.append(name)
            self.neighbors.sort()


class Graph:
    vertexs = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertexs:
            self.vertexs[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertexs and v in self.vertexs:
            for key, value in self.vertexs.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in self.vertexs:
            print(f'{key}: {str(self.vertexs[key].neighbors)}')


def main():
    graph = Graph()

    for i in range(ord('A'), ord('K')):
        graph.add_vertex(Vertex(chr(i)))

    edgs = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FJ', 'GJ','HI']
    for edg in edgs:
        graph.add_edge(edg[0], edg[1])

    graph.print_graph()

main()



