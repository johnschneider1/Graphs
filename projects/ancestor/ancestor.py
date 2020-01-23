from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # do a bfs (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # if path is longer or equal and the value is smaller or if the path is longer
        # do the thing 51 minutes into lecture
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor
