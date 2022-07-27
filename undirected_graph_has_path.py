"""
Given a list of edges (E) for an undirected graph, each representing a connection between two nodes, and given two specific nodes, 
detect if there is a path between them.

- First is important to conver the edges structure into an adjacency list graph representation, both in code and graphical (as below):

edges : [
    [i, j],
    [k, i],
    [m, k],
    [k, l],
    [o, n],
]

Converts to a Adjacency List based Graph as:

graph: {
    "i": ["j", "k"],
    "j": ["i"],
    "k": ["i", "m", "l"],
    "m": ["k"],
    "l": ["k"],
    "o": ["n"],
    "n": ["o"]    
}

- Secondly, is also important to consider the edge case in which the UNDIRECTED graph has a cycle, which could create an infite loop, with no exit condition.

- Complexity:
    - Time: O(e)
    - Space: O(n)

"""

# The edges are pairs in a list, they connect only two nodes
def convert_edges_to_graph(edges):
    graph = {}

    for edge_list in edges:
        a = edge_list[0]
        b = edge_list[1]

        if a not in graph:
           graph[a] = [] 
        if b not in graph:
           graph[b] = [] 
        
        graph[a].append(b)
        graph[b].append(a)
            
    print(graph)
    return graph

def has_path_undirected(graph, start, destination):
    #Keeps track of visited nodes, to avoid cycles, and enhance performance
    visited = []
    queue = []
    queue.append(start)
    visited.append(start)
    
    while queue:
        current = queue.pop()

        if destination == current:
            return True

        for neighbour in graph[current]:
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

    return False

def run_example():
    """
    Graphical Crude View:

        i --- j
        |     
        |     
        |     
        k --- l 
        |
        |
        m

        o --- n
        

    """
    edges = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"]
    ]

    source = "k"
    destination = "j"
    graph = convert_edges_to_graph(edges)
    has_path = has_path_undirected(graph, source, destination)
    print(f"Path between node {source} and node {destination} ? {has_path}")

def main():
    run_example()
    print()

if __name__ == "__main__":
    main()
