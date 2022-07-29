from collections import deque

"""
Given a graph structure, count and return the number of connected components. This basically means how many "sub-graphs" there
are in a given Graph like structure.

- The idea is to loop through the Graph's nodes as sources, all of them, but also keep a visited Set or Map, that can be used to check if, as we go along, any of the nodes were
already visited using DFS or BFS. This algorithm changes the implementation slightly to return a list of visited nodes pero sub-graph traversed (triggered by the alternating source
nodes.)

Important 1:


Complexity:
    - Time: O(E) if all nodes are their own sub-graphs
    - Space: O(N), if the visited ones size is the same as the total number of nodes in original Graph.
"""



def modified_depth_first_search(graph, source):
    visited = set()
    stack = deque()
    stack.append(source)

    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            # print(current) # For tracking / illustration purposes
            for neighbour in graph[current]:
                stack.append(neighbour)

    return visited #return list of traversed per iteration

# iterate and merge with returned list of traversed from above function output, then return number of connected components or sub-graphs.
def connected_components(graph):
    visited = set() #Python Set, 0(1) for deletion and insertion (uses Hashing techniques)
    components = 0

    for node in graph:
        if node not in visited:
            visited.update(modified_depth_first_search(graph, node))
            components+=1
    
    return components

def main():
    # Graph represented as Python dick (Map in Java) with adjacency list for a Node's neighbours
    # graph = {
    #     "1": ['2'],
    #     "2": ['1'],
    #     "3": [],
    #     "4": ['6'],
    #     "5": ['6'],
    #     "6": ['4', '5', '7', '8'],
    #     "7": ['6'],
    #     "8": ['6']
    # }

    # Edge case Graph: Empty Graph
    # graph = {
    #     "1": [],
    #     "3": [],
    #     "4": []
    # }

    # One subcomponent or subgraph
    graph = {
        "1": ['2'],
        "2": ['1']
    }

    components = connected_components(graph)
    print(f"Number of Connected components (subgraphs): {components}")

if __name__ == "__main__":
    main()