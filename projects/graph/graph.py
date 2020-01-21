"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        intakes vertex id which is a number 
        """
        self.vertices[vertex_id] = set()  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That index does not exisit")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.veertices[vertex_id]  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create an empty queue and enqueue the starting vertex ID
        # create an empty set to store visited vertices
        # #while the queue is not empty...
        # dequeu the first vertex
        # if that vertex has not been visisted
        # mark it as visited
        # then add all its neighbors to the back of the queue
        #   # TODO
        # create an empty stack and push the starting vertex ID
        queue = Queue()
        # put the starting point in that
        queue.enqueue(starting_vertex)
        # create an empty set to store visited vertices
        visited = set()

        # #while the stack is not empty...
        while queue.size() > 0:
            # pop the first vertex
            vertex = queue.dequeue()

        # if that vertex has not been visisted
            if vertex not in visited:

                # mark it as visited
                print(vertex)
                visited.add(vertex)
        # then add all its neighbors to the back of the stack
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

        # q = Queue()
        # q.enqueue(starting_vertex)
        # visited = set()
        # while q.size() > 0:
        #     vertex = q.dequeue()
        #     if vertex not in visited:
        #         print(vertex)
        #         visited.add(vertex)
        #         for neighbor in self.vertices(vertex):
        #             q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
      # create an empty stack and push the starting vertex ID
        stack = Stack()
        # put the starting point in that
        stack.push(starting_vertex)
        # create an empty set to store visited vertices
        visited = set()

        # #while the stack is not empty...
        while stack.size() > 0:
            # pop the first vertex
            vertex = stack.pop()

        # if that vertex has not been visisted
            if vertex not in visited:

                # mark it as visited
                print(vertex)
                visited.add(vertex)
        # then add all its neighbors to the back of the stack
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push the starting vertex ID
        stack = Stack()
        # put the starting point in that
        stack.push(starting_vertex)
        # create an empty set to store visited vertices
        visited = set()

        # #while the stack is not empty...
        while stack.size() > 0:
            # pop the first vertex
            vertex = stack.pop()
            if vertex == destination_vertex:
                return
            vertex = stack.pop()

        # if that vertex has not been visisted
            # if vertex not in visited:

            #     # mark it as visited
            #     print(vertex)
            visited.add(vertex)
        # then add all its neighbors to the back of the stack
            for neighbor in self.vertices[vertex]:
                stack.push(neighbor)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Printintg graph vertices")
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
