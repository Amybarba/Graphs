"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


# What type of graph does git use? a directed acyclic

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # this is our adjacency list(empty dict)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        # why use a set? only one connection for each edge, no duplicates

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # make code robust and flexible and check if they exist first
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")
            # no return needed because python implicitly return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # might want to crash program to raise an exception here instead

    # search is looking till you find a specific node, traversal is visiting each node

    # one step at a time, like an array,layer by layer, or connection by connection
    # a breadth first search will give you the shortest path to any node, a breadth first
    # traversal will give you the shortest path from one node to all the other nodes
    # good for solving a maze or finding the shortest path like maps

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue(starting_vertex)
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            current_node = qq.dequeue()
            # if not visited
            if current_node not in visited:
                # DO THE THING!!!!
                # mark as visited
                visited.add(current_node)
                # print it
                print(current_node)
                # enqueue all the neighbors
                neighbors = self.get_neighbors(current_node)
                # list is a python constrictor that creates a new list
                # must create a new path, not add to the path, otherwise you alter the list, not good
                for neighbor in neighbors:
                    qq.enqueue(neighbor)

    # find the optimal starting point of source you want to connect to all nodes, then go to each node and its
    # connections minimum spanning tree

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack with the starting vertex
        ss = Stack()
        ss.push(starting_vertex)
        # create a set of traversed vertices
        visited = set()
        # while stack is not empty:
        while ss.size() > 0:
            # pop off the top of the stack, creates our current node
            current_node = ss.pop()
            # if not visited
            if current_node not in visited:
                # DO THE THING!!!!

                # mark as visited
                visited.add(current_node)
                # print it
                print(current_node)
                # get all the neighbors
                neighbors = self.get_neighbors(current_node)
                # list is a python constrictor that creates a new list
                # must create a new path, not add to the path, otherwise you alter the list, not good
                for neighbor in neighbors:
                    ss.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        # need another paremeter
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # every recursive code needs an initial case
        if visited is None:
            visited = set()

        # every recursive needs a base case, how do we know we are done? no more neighbors

        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # call the function recursively  - on neighbors not visited
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        qq = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        qq.enqueue(path)
        # while queue isn't empty
        while qq.size() > 0:
            # dequeue the node at the front of the line
            current_path = qq.dequeue()
            current_node = current_path[-1]
            # if this node is our target node
            if current_node == destination_vertex:
                # return it, return TRUE
                return current_path
            #  if not visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each neighbor
                for neighbor in neighbors:
                    # copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    # add to our queue
                    qq.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        path = []
        ss = Stack()
        ss.push(starting_vertex)
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            newnode = ss.pop()
            # if not visited
            if newnode not in visited:
                # mark as visited
                visited.add(newnode)
                # get all the neighbors
                path.append(newnode)
                if newnode == destination_vertex:
                    return path
                # must create a new path, not add to the path, otherwise you alter the list, not good
                for neighbor in self.get_neighbors(newnode):
                    ss.push(neighbor)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # every recursive code needs an initial case
        if visited is None:
            visited = set()

        if path is None:
            path = []

        # every recursive needs a base case, how do we know we are done? no more neighbors

        # track visited nodes
        visited.add(starting_vertex)
        # make a copy of the path
        new_path = path + [starting_vertex]

        # DO THE THING!
        if starting_vertex == destination_vertex:
            return new_path
        # this is a base case
        # call the function recursively - on neighors not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path


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
