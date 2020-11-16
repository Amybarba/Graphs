<<<<<<< HEAD
# alternate solution by creating classes, longer, messier
class Queue:
    def __init__(self):
        # capture the list of nodes
        self.queue = []

    def enqueue(self, value):
        # add the value to the list
        self.queue.append(value)

    def dequeue(self):
        # safeguard you are getting a return by setting the parameters
=======
# Solution by creating multiple classes, longer, messier
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
<<<<<<< HEAD
        # create a way to define what size you are getting back
        return len(self.queue)


class Graph:
    # capture the edges
=======
        return len(self.queue)


class Graph():
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
<<<<<<< HEAD
        # safeguard that you are getting the edges represented in the set
=======
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
<<<<<<< HEAD
        # make sure each edge is connected to the other or throw an error
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    # now that the parameters are set build your graph here
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

        # build edges but start at the bottom
        g.add_edges(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])
=======
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    # build our graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges in reverse
        graph.add_edges(pair[1], pair[0])

    qq = Queue()
    qq.enqueue([starting_node])
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83

    max_path_length = 1
    earliest_ancestor = -1

<<<<<<< HEAD
    while q.size() > 0:
        path = q.dequeue()
=======
    while qq.size() > 0:
        path = qq.dequeue()
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83
        v = path[-1]

        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

<<<<<<< HEAD
        for neighbor in g.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


# target is the earliest ancestor so a Depth First Search would work
# create a stack class first

class Stack:
    # create a place for your list of ancestors
    def __init__(self):
        self.stack = []

    # add to the stack to pick up nodes
    def push(self, value):
        self.stack.append(value)

    # take of stack values not needed
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]] = [pair[0]]

    s = Stack()
    visited = set()
    s.push([starting_node])
    a_len = 0

    if starting_node not in graph:
        return -1
    while s.size() > 0:
        path = s.pop()
        node = path[-1]
        if node in graph:
            for parent in graph[node]:
                new_path = list(path)
                new_path.append(parent)
                s.push(new_path)
                if new_path == 0:
                    earliest_ancestor = min(earliest_ancestor, parent)
                elif len(new_path) > a_len:
                    earliest_ancestor = parent
                    a_len = len(new_path)
    return earliest_ancestor
=======
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            qq.enqueue(path_copy)

    return earliest_ancestor

# target is the earliest ancestor so a Depth First Search would work
# create only one class, a stack class first


# class Stack:
#    def __init__(self):
#        self.stack = []

# add to the stack to pick up nodes

#    def push(self, value):
#        self.stack.append(value)
# take off the stack values not needed

#    def pop(self):
#        if self.size() > 0:
#            return self.stack.pop()
#        else:
#            return None

#    def size(self):
#        return len(self.stack)


# def earliest_ancestor(ancestors, starting_node):
#    graph = {}
#    for pair in ancestors:
#        if pair[1] in graph:
#            graph[pair[1]].append(pair[0])
#        else:
#            graph[pair[1]] = [pair[0]]

#    stack = Stack()
#    visited = set()
#    stack.push([starting_node])
#    a_len = 0

#    if starting_node not in graph:
#        return -1
#    while stack.size() > 0:
#        path = stack.pop()
#        node = path[-1]
#        if node in graph:
#            for parent in graph[node]:
#                new_path = list(path)
#                new_path.append(parent)
#                stack.push(new_path)
#                if new_path == 0:
#                    earliest_ancestor = min(earliest_ancestor, parent)
#                elif len(new_path) > a_len:
#                    earliest_ancestor = parent
#                    a_len = len(new_path)
#    return earliest_ancestor
>>>>>>> 0b4466b84f4cade17f8a022f1c6ff69b27c84b83
