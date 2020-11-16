"""Write a function that takes a 2D Binary array and returns the number of 1 island
An island consists of 1's connected N, S, E, W
for example the island example returns 4 here

islands =
[ [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1],
  [0, 0, 1, 0, 0],
  [1, 0, 1, 0, 0],
  [1, 1, 0, 0, 0]]
What is tricky about working with 2 dimensional arrays
x and y flipped
you need to do
y , x

shape of solution for 2d array the matrix will always
be square

where is our graph? no edges
do I need to turn this into a system of nodes and edges or
what can I do instead?
Do it Adhock - get neighbors function
Write a get neighbor function that uses this shape?
We can offset coordinates to get the neighbors
call get neighbors on this node and look nsew
and if visited ignore it
any of 1's or 0's can be found using
island[y][x]
we could use recursion or traversal methods
diagonals do not count as sharing

example solution 1:

def get_neighbors(matrix, node_x, node_y, size):
    neighbors = []
    if node_y > 0:
        n_neighbor = (node_y -1, node_x)
        neighbors.append(n_neighbor)
    if node_x > 0:
        w_neighbor - (node_y, node_x -1)
        neighbors.append(w_neighbor)
    if node_y < size -1:
        s_neighbor = (node_y +1, node_x)
        neighbors.append(s_neighbor)
    if node_x < size -1:
        e_neighbor = (node_y, node_x +1)
        neighbors.append(e_neighbor)
    return neighbors

def dft_traversal_recursive(matrix, node_x, node_y, size, visited):
    neighbors = get_neighbors(matrix, node_x, node_y, size)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            neighbor_x = neighbor[0]
            neighbor_y = neighbor[1]
            if matrix[neighbor_x][neighbor_y] == 1:
                dft_traversal_recursive(matrix, neighbor_x, neighbor_y, size, visited)


def find_islands(matrix):
    size = len(matrix)
    visited = set()
    islands = 0
    for i in range(size):
        for j in range(size):
            if (i, j) not in visited:
                visited.add((i, j))
                if matrix[i][j] == 1:
                    dft_traversal_recursive(matrix, j, i, size, visited)
                    islands += 1
    return islands


 islands = [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]

print(find_islands(islands))

example solution 2:
"""


# islands consists of - connected components
# connected - neighbors (connected to neighbors by edges)
# directions, nsew (edges)
# 2d array - this is the graph, not quite the shape
# returns (shape of solution) - number of islands

# write a get neighbor function that offsets coordinates

# Loop through and call a traversal if we find an unvisited 1



