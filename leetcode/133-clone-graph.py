# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# Time: O(V + E) We did a modified DFS
# Space: O(V) Due to our stack. Becomes O(V + E) if you include Result Clone Graph
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        node_clone = Node(node.val, [])
        visited[node] = node_clone

        stack = [node]
        while stack:
            popped = stack.pop()
            for neighbor in popped.neighbors:
                if neighbor not in visited:
                    neighbor_clone = Node(neighbor.val, [])
                    visited[neighbor] = neighbor_clone
                    stack.append(neighbor)
                visited[popped].neighbors.append(visited[neighbor])

        return node_clone