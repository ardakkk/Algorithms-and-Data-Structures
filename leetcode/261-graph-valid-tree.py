# Time: O(V + E) Same time complexity as a DFS.
# Space: O(V + E) We stored our Graph as an Adjacency List.

class Solution:
    def isValidTree(self, N, edges):
        adjacency_list = {}
        visited = {}

        for vertex in range(N):
            adjacency_list[vertex] = []
            visited[vertex] = False

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        def dfs(vertex, parent):  # returns true if cycle detected and vice versa
            visited[vertex] = True

            for neighbor_vertex in adjacency_list[vertex]:
                if not visited[neighbor_vertex]:
                    if dfs(neighbor_vertex, vertex):
                        return True
                else:
                    if neighbor_vertex != parent:
                        return True

            return False

        if dfs(0, -1):
            return False

        for vertex in range(N):
            if not visited[vertex]:
                return False

        return True

