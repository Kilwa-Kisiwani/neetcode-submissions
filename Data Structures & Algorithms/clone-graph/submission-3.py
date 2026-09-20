"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def drawGraph(node: Optional['Node'], node_map) -> Optional['Node']:
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val, [])
            node_map[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in node_map:
                    new_node.neighbors.append(node_map[neighbor])
                else:
                    new_node.neighbors.append(drawGraph(neighbor, node_map))
            return new_node
                

 
            


        return drawGraph(node, {})
            
            
            