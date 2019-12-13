# Given n nodes labeled from 0 to n-1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to find the number
# of connected components in an undirected graph.


# Example 1:
# 0          3
# |          |
# 1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
# 0          4
# |          |
# 1 --- 2 -- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

# Time: O(V + E) We do simple DFS for given graph
# Space: O(V + E) We stored our Graph as an Adjacency List.
class Solution:
    def countComponents(self, N, edges):
        adjacency_list = {}
        visited = {}
        count = 0

        for vertex in range(N):
            visited[vertex] = False
            adjacency_list[vertex] = []

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]


            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        def dfs(vertex):
            visited[vertex] = True

            for neighbour_vertex in adjacency_list[vertex]:
                if not visited[neighbour_vertex]:
                    dfs(neighbour_vertex)

        for vertex in range(N):
            if not visited[vertex]:
                dfs(vertex)
                count += 1

        return count
