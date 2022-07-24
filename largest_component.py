from queue import Queue

'''
Given a Graph structure (undirected or directed, the former could have cycles), that could contain separate components (sub-graph), return the size of the component 
with the largest size (number of nodes).

Complexity:
    - Time: O(E) if all nodes are their own sub-graphs
    - Space: O(N), if the visited ones size is the same as the total number of nodes in original Graph
'''

# Uses DFS
def calculate_graph_size_DFS(graph, node, visited):
    queue = Queue(0) # In Python, Queue object of size 0 upon initialization means undefined number of places for the queue
    queue.put(node)
    component_size = 0

    while queue.qsize() > 0:
        current = queue.get()
        if current not in visited:  # This check could also go at the beginning of the function...and avoids the first iteration, but this is negligeable.
            visited.update(current)
            component_size += 1
            for neighbour in graph[current]:
                queue.put(neighbour)
            
    return component_size

def largest_component(graph):
    visited = set()
    largest_component = 0

    for node in graph:
        if node not in visited:
            component_size = calculate_graph_size_DFS(graph, node, visited)
        if component_size > largest_component:
            largest_component = component_size

    return component_size


def main():

    # Graph represented as Python dict (Map in Java) with adjacency list for a Node's neighbours
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
    graph = {
        "1": [],
        "3": [],
        "4": []
    }

    largest = largest_component(graph)
    print(f'Largest component (sub-graph) size: {largest}')

if __name__ == "__main__":
    main()