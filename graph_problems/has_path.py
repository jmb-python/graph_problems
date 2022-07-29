from collections import deque

"""
Problem: Having a directed and acyclic graph, find out if two given nodes have a path (indirectly/directly connected) between them.
Either DFS and BFS can be used, this algorithm uses DFS.

Logic: Traverse the nodes with DFS, and if the current node (in whatever traversing iteration) is equals to the destination node, then return True.
Otherwise there is no connection, return False.

Complexity: 
    Time - O(e), where e = edges. Basically in the worst case scenario we would have to travel through every edge in the graph, also in this case, number of e = n pow 2.
    Space - O(n), where n = nodes. Takes the space needed to store all the nodes in the Graph dictionary structure (see below).
"""

def has_path(graph, source, destination):
    stack = deque()
    stack.append(source)

    while len(stack) > 0:
        current = stack.pop()
        
        if current == destination:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)        

    return False

def has_path_recursive(graph, source, destination):
    # base recursion case
    if source == destination:
        return True
    
    for neighbour in graph[source]:
        if has_path_recursive(graph, neighbour, destination) is True:
            return True

    return False

def run_example():
    """
    Graphical Crude View:

        f ---> g ---> h
        |    ^ |
        |   /  |
        |  /   |
        V /    V
        i <--- j
        |
        |
        V
        k

    """
    
    # Graph represented as Python dick (Map in Java) with adjacency list for a Node's neighbours
    graph = {
        "f": ['g', 'i'],
        "g": ['h', 'j'],
        "h": [],
        "i": ['k'],
        "j": ['i'],
        "k": []
    }

    return has_path_recursive(graph, "f", "j")

def main():
    print("Path between nodes j and f ? : ")
    print(run_example())

if __name__ == "__main__":
    main()