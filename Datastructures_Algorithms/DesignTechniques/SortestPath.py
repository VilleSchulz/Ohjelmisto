class Vertex:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Vertex: {self.name}>"  # Custom string representation to match your desired format


class Edge:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight


class Graph:
    def __init__(self, adj_map):
        self.adj_map = adj_map

    def get_vertices(self):
        return list(self.adj_map.keys())

    def get_edges(self, vertex):
        return self.adj_map.get(vertex, {})


def dijkstra_shortest_path(start, end, graph):
    # Initialize the shortest path table with infinity and no previous vertices
    shortest_path_table = {vertex: {'shortest': float('inf'), 'previous': None} for vertex in graph.get_vertices()}
    shortest_path_table[start]['shortest'] = 0
    unvisited_vertices = list(graph.get_vertices())

    while unvisited_vertices:
        # Find the vertex with the smallest distance in the unvisited set
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_path_table[vertex]['shortest'])
        unvisited_vertices.remove(current_vertex)

        # If we've reached the end vertex, we can stop
        if current_vertex == end:
            break

        # Explore the neighbors of the current vertex
        for neighbor, edge in graph.get_edges(current_vertex).items():
            alternative_route = shortest_path_table[current_vertex]['shortest'] + edge.weight
            if alternative_route < shortest_path_table[neighbor]['shortest']:
                shortest_path_table[neighbor]['shortest'] = alternative_route
                shortest_path_table[neighbor]['previous'] = current_vertex

    # Reconstruct the shortest path by tracing the 'previous' pointers
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.insert(0, current_vertex)  # Insert at the beginning to reverse the order
        current_vertex = shortest_path_table[current_vertex]['previous']

    # Return the shortest path and its length
    return shortest_path_table[end]['shortest'], path


