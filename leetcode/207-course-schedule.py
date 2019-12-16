# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def canFinish(self, N: int, edges: List[List[int]]) -> bool:
        adjacency_list = {}
        visited = {}

        for vertex in range(N):
            adjacency_list[vertex] = []
            visited[vertex] = "white"

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            adjacency_list[v1].append(v2)

        # Returns true if cycle detected and vice versa
        def dfs(vertex):
            visited[vertex] = "gray"

            for neighbour_vertex in adjacency_list[vertex]:
                if visited[neighbour_vertex] == "gray":
                    return True
                if visited[neighbour_vertex] == "white" and dfs(neighbour_vertex):
                    return True

            visited[vertex] = "black"
            return False

        for vertex in range(N):
            if visited[vertex] == "white":
                if dfs(vertex):
                    return False

        return True
