from collections import deque

''' Picks a starting node in a Graph, pushes it to the stack as the first element there.
    Then, adds the node's neighbours to the stack, in arbitrary order. Then picks the next object in the stack and repeats the process. This guarantees a specific order
    of traversing (follows always the first neightbours of each node once we start with a node path), but it includes eventually all the nodes being visited in depth.
    and moves in another direction repeating the same pattern until all the Graph is visited.
    
    Important 1: It also keeps track of nodes already visited, to avoid visiting them again, if another traversing iteration already went there, from a different node.
    
    Important 2: The algorithm changes slightly depending on whether we print the already visited node or not. Another map (O(1)) could be used to check if it was already visited.

    KEY_TO_REMEMBER: Uses a STACK structure to "remember" its previous steps.
'''

def depth_first_traverse(graph, start_node):
    # deque structure from Python libraries used as stack (double ended queue: https://en.wikipedia.org/wiki/Double-ended_queue)
    stack = deque()
    stack.append(start_node)

    while len(stack) > 0:
        current = stack.pop()
        print(current)        
        for neighbour in graph[current]:
            stack.append(neighbour)


# Recursive version of the algorithm, but if the Graph is massive, this might incurr in StackOverflow type of errors.
def depth_first_traverse_recursive(graph, node):
    
    for neighbour in graph[node]:
        depth_first_traverse_recursive(graph, neighbour)


def run_example():
    """
    Graphical Crude View:

        A --- C
        |     |
        |     |
        B     E
        |
        |
        D --- F

    """
    
    # Graph represented as Python dick (Map in Java) with adjacency list for a Node's neighbours
    graph = {
        "a": ['c', 'b'],
        "b": ['d'],
        "c": ['e'],
        "d": ['f'],
        "e": [],
        "f": []
    }

    depth_first_traverse(graph, "a")
    print()
    depth_first_traverse_recursive(graph, "a")

def main():
    run_example()

if __name__ == "__main__":
    main()