"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.visit(node,{})
        
    
    def visit(self, current, visited):
        if current is None:
            return None

        if current in visited:
            return visited[current]

        new = Node(current.val)
        visited[current] = new
        
        for el in current.neighbors:
            new.neighbors.append(self.visit(el, visited))

        return new