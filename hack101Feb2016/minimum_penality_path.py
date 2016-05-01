INFINITY = 1025  # Given the max cost of any edge is 1024


class Vertex:
    def __init__(self, key, d):
        self.k = key
        self.d = d

    def __str__(self):
        return str(self.key)


class Graph:
    def __init__(self, edge_list):
        self.adj = {}
        self.edges = {}
        self.v = []
        self.add_edges(edge_list)

    def upsert(self, h, k, v):
        if k in h:
            h[k].append(v)
        else:
            h[k] = [v]

    def add_edges(self, edge_list):
        existing_v = set(self.v)
        for e in edge_list:
            self.upsert(self.adj, e[0], e[1])
            self.upsert(self.adj, e[1], e[0])
            self.edges[(e[0], e[1])] = e[2]
            self.v.append(Vertex(e[0], INFINITY))
            self.v.append(Vertex(e[1], INFINITY))
        self.v = list(set(self.v))  # eliminate duplicates

    def adj(self, v):
        return self.adj[v]

    def __str__(self):
        return str(self.v)


def create_graph(edge_list):
    G = Graph(edge_list)
    return G


def dijkstras(G):
    pass


def run():
    edge_list = [(1, 2, 1), (1, 2, 1000), (2, 3, 3), (1, 3, 100)]
    create_graph(edge_list)


if __name__ == '__main__':
    run()
