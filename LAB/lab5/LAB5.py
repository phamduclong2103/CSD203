# Exercise 1: Create text files to store the adjacency matrix of a graph in Figure 1 and write the Graph class.
class Graph:
    def __init__(self):
        self.a = []  # two-dimensional array representing an adjacency matrix
        self.label = []  # label of vertices
        self.n = 0  # number of vertices

    def setAMatrix(self, b, m):
        self.n = m
        self.a = b

    def setLabel(self, c):
        self.label = c

    def breadthFirstTraverse(self, start_vertex):
        visited = [False] * self.n
        queue = []

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(self.label[vertex], end=" ")

            for i in range(self.n):
                if self.a[vertex][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def depthFirstTraverse(self, start_vertex):
        visited = [False] * self.n

        def dfs(vertex):
            visited[vertex] = True
            print(self.label[vertex], end=" ")

            for i in range(self.n):
                if self.a[vertex][i] == 1 and not visited[i]:
                    dfs(i)

        dfs(start_vertex)

# # Create a graph object
# graph = Graph()

# # Set the adjacency matrix
# adjacency_matrix = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1, 0, 0, 0]
#     [0, 0, 0, 0, 0, 1, 0, 0, 0]
#     [0, 0, 0, 1, 1, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0, 1, 1]
#     [0, 0, 0, 0, 0, 0, 1, 0, 0]
#     [0, 0, 0, 0, 0, 0, 1, 0, 0]
# ]
# graph.setAMatrix(adjacency_matrix, 9)

# # Set the labels for vertices
# labels = ["A", "B", "C", "D","E","F","G","H","I"]
# graph.setLabel(labels)

# # Perform breadth-first traversal starting from vertex 0
# print("Breadth-First Traversal:")
# graph.breadthFirstTraverse(0)
# print()

# # Perform depth-first traversal starting from vertex 2
# print("Depth-First Traversal:")
# graph.depthFirstTraverse(2)
# print()

# Set the graph matrix
graph_matrix = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
]

graph_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# Create a Graph object
graph = Graph()

# Set the adjacency matrix
graph.setAMatrix(graph_matrix, len(graph_matrix))

# Set the labels of vertices
graph.setLabel(graph_labels)

# Perform breadth-first traversal starting from vertex 0
print("Breadth-First Traversal:")
graph.breadthFirstTraverse(0)
print()

# Perform depth-first traversal starting from vertex 0
print("Depth-First Traversal:")
graph.depthFirstTraverse(0)
print()

# Exercise 2: Write the WGraph class with Dijkstra's shortest path algorithm.
import sys

class WGraph:
    def __init__(self):
        self.w = []    # two-dimensional array representing a weighted matrix
        self.n = 0    # number of vertices

    def setWMatrix(self, b, m):
        self.n = m
        self.w = b

    def dijkstraShortestPath(self, start_vertex):
        # Tạo danh sách để lưu trữ khoảng cách ngắn nhất từ ​​đỉnh bắt đầu đến tất cả các đỉnh khá
        distance = [sys.maxsize] * self.n
        distance[start_vertex] = 0

        # Tạo một danh sách để theo dõi các đỉnh đã truy cập
        visited = [False] * self.n

        for _ in range(self.n):
            # Tìm đỉnh có khoảng cách nhỏ nhất từ ​​tập hợp các đỉnh chưa được thăm
            min_distance = sys.maxsize
            min_vertex = -1

            for v in range(self.n):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_vertex = v

            # Đánh dấu đỉnh đã chọn là đã truy cập
            visited[min_vertex] = True

            # Cập nhật giá trị khoảng cách của các đỉnh liền kề
            for v in range(self.n):
                if (
                    not visited[v]
                    and self.w[min_vertex][v] != 0
                    and distance[min_vertex] + self.w[min_vertex][v] < distance[v]
                ):
                    distance[v] = distance[min_vertex] + self.w[min_vertex][v]

        return distance

# Create an instance of the WGraph class
graph = WGraph()

# Set the weighted matrix
weight_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
graph.setWMatrix(weight_matrix, len(weight_matrix))

# Perform Dijkstra's algorithm to find the shortest paths from vertex 0
start_vertex = 0
shortest_distances = graph.dijkstraShortestPath(start_vertex)

# Print the shortest distances
print("Shortest Distances from vertex", start_vertex)
for i, distance in enumerate(shortest_distances):
    print("To vertex", i, ":", distance)

#Exercise 3: Write the WGraph class with methods for finding the minimum spanning tree of a graph.
class WGraph:
    def __init__(self):
        self.w = []  # Weighted matrix
        self.n = 0   # Number of vertices

    def setWMatrix(self, b, m):
        self.n = m
        self.w = b

    def findMinimumSpanningTree(self):
        # Initialize an empty list to store the minimum spanning tree
        mst = []

        # Initialize a list to keep track of vertices included in the minimum spanning tree
        included = [False] * self.n

        # Start with the first vertex
        included[0] = True

        # Repeat the following steps (n-1) times, where n is the number of vertices
        for _ in range(self.n - 1):
            min_weight = float('inf')
            min_edge = None

            # Find the minimum-weight edge that connects an included vertex to an excluded vertex
            for i in range(self.n):
                if included[i]:
                    for j in range(self.n):
                        if not included[j] and self.w[i][j] != 0 and self.w[i][j] < min_weight:
                            min_weight = self.w[i][j]
                            min_edge = (i, j)

            # Add the minimum-weight edge to the minimum spanning tree
            mst.append(min_edge)

            # Include the newly added vertex in the included list
            included[min_edge[1]] = True

        return mst

# Create an instance of the WGraph class
graph = WGraph()

# Set the weighted matrix
weighted_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
graph.setWMatrix(weighted_matrix, 9)

# Find the minimum spanning tree
minimum_spanning_tree = graph.findMinimumSpanningTree()

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    vertex1 = edge[0]
    vertex2 = edge[1]
    print(f"Edge: {vertex1} - {vertex2}")

#Exercise 4: Write the Graph class with the sequential coloring algorithm.
class Graph:
    def __init__(self):
        self.a = []  # Adjacency matrix
        self.label = []  # Labels of vertices
        self.n = 0  # Number of vertices

    def setAMatrix(self, b, m):
        self.n = m
        self.a = b

    def setLabel(self, c):
        self.label = c

    def assignColors(self):
        colors = [0] * self.n  # Initialize color array

        for vertex in range(self.n):
            # Create a set of colors used by adjacent vertices
            used_colors = set()

            # Traverse the adjacent vertices
            for adj_vertex in range(self.n):
                if self.a[vertex][adj_vertex] == 1 and colors[adj_vertex] != 0:
                    used_colors.add(colors[adj_vertex])

            # Find the first available color for the vertex
            for color in range(1, self.n + 1):
                if color not in used_colors:
                    colors[vertex] = color
                    break

        return colors
# Create an instance of the Graph class
graph = Graph()

# Set the adjacency matrix
adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
graph.setAMatrix(adjacency_matrix, 5)

# Set the labels of vertices
labels = ['A', 'B', 'C', 'D', 'E']
graph.setLabel(labels)

# Assign colors to vertices
colors = graph.assignColors()

# Print the colors assigned to vertices
print("Colors assigned to vertices:")
for i, color in enumerate(colors):
    vertex = graph.label[i]
    print(f"{vertex}: Color {color}")
