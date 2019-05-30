"""
Implement graph using adjacency matrix
"""


class Vertex():
    def __init__(self, name):
        self.name = name


class Graph():
    vertexs = {}
    edgs = []
    edg_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertexs:
            self.vertexs[vertex.name] = vertex
            for row in self.edgs:
                row.append(0)
            self.edgs.append([0] * (len(self.edg_indices) + 1))
            self.edg_indices[vertex.name] = len(self.edg_indices)
            return True
        else:
            return False

    def add_edg(self, u, v, weight=1):
        if u in self.vertexs and v in self.vertexs:
            self.edgs[self.edg_indices[u]][self.edg_indices[v]] = weight
            self.edgs[self.edg_indices[v]][self.edg_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in self.edg_indices.items():
            print(v, end='  ')
            for j in range(len(self.edgs)):
                print(self.edgs[i][j], end=' ')
            print('')


def main():
    graph = Graph()

    for i in range(ord('A'), ord('K')):
        graph.add_vertex(Vertex(chr(i)))

    edgs = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FJ', 'GJ','HI']
    for edg in edgs:
        graph.add_edg(edg[0], edg[1])

    graph.print_graph()

main()