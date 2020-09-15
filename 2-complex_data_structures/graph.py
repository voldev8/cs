class Graph:
    '''
    Can be initialized as a directed graph, where edges are set in one direction.
    Stores every vertex inside a dictionary
    Vertex data is the key and the vertex instance is the value.
    '''

    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    # Has methods to add vertices, edges between vertices, and determine if a path exists between two vertices.

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(
                    self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False


class Vertex:
    ''' 
    Uses a dictionary as an adjacency list to store connected vertices.
    Connected vertex names are keys and the edge weights are values.
    '''

    def __init__(self, value):
        self.value = value
        self.edges = {}
    # Has methods to add edges and return a list of connected vertices

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())
