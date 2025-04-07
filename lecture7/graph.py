'''
Tree is a connected acyclic graph
'''
'''
Adjacency list :
        an adjacency list is a collection of unordered list used to represent a graph.
    each list describes the set of neighbors of a vertex in a graph
    if a graph is complete or almost complete we shoulf use adjacency matrix.
    if the number of edges are few we should use adjacency list
'''

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1,  vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","C")
my_graph.add_edge("C","D")
my_graph.add_edge("E","B")
my_graph.add_edge("D","A")
my_graph.add_edge("D","C")
my_graph.add_edge("D","E")
my_graph.print_graph()