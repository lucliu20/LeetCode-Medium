# https://leetcode.com/problems/clone-graph/

"""
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example 4:
Input: adjList = [[2],[1]]
Output: [[2],[1]]
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Preparation work:
# implementation of an undirected graph using Adjacency Lists
# class Node:
# 	def __init__(self, n, neighbors = None):
# 		self.name = n
# 		self.neighbors = neighbors if neighbors is not None else []
# 	
# 	def add_neighbor(self, v):
# 		if v not in self.neighbors:
# 			self.neighbors.append((v))
# 			# self.neighbors.sort()
# 
# class Graph:
# 	vertices = {}
# 	
# 	def add_node(self, vertex):
# 		if isinstance(vertex, Node) and vertex.name not in self.vertices:
# 			self.vertices[vertex.name] = vertex
# 			return True
# 		else:
# 			return False
# 	
# 	def add_edge(self, u, v):
# 		if u in self.vertices and v in self.vertices:
# 			self.vertices[u].add_neighbor(v)
# 			self.vertices[v].add_neighbor(u)
# 			return True
# 		else:
# 			return False
# 
# g = Graph()
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# g.add_node(a)
# g.add_node(b)
# g.add_node(c)
# g.add_node(d)
# a.add_neighbor(b)
# b.add_neighbor(c)
# c.add_neighbor(d)
# d.add_neighbor(a)
# a.add_neighbor(d)
# b.add_neighbor(a)
# c.add_neighbor(b)
# d.add_neighbor(c)
# 
# edges = [(1,2), (1,4), (2,3), (3,4)]
# for i, j in edges:
# 	g.add_edge(i, j)
# 
# print(g.vertices[1])
# print(node)


# Refer to the video clip below for iterative version
# https://www.youtube.com/watch?v=L6duXCKa-d4

# Refer to the post below:
# https://leetcode.com/problems/clone-graph/discuss/902767/Python-dfs-recursive-solution-explained
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         def dfs(node):
#             mapping[node] = Node(node.name)
#             for neigh in node.neighbors:
#                 if neigh not in mapping: dfs(neigh)
#                 mapping[node].neighbors += [mapping[neigh]]
#         
#         if not node: return node
#         mapping  = {}
#         dfs(node)
#         return mapping[node]

# Refer to the video clip:
# https://www.youtube.com/watch?v=vma9tCQUXk8
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        seen = {} # Key: node_value; Value: new_node_reference
        def dfs(node):
            new_node = Node(node.val)
            seen[node.val] = new_node
            new_neighbors = []
            for nei in node.neighbors:
                if nei.val not in seen:
                    new_neighbors.append(dfs(nei))
                else:
                    new_neighbors.append(seen[nei.val])
            new_node.neighbors = new_neighbors
            return new_node
        return dfs(node)

solution = Solution()
solution.cloneGraph(node)

# Runtime: 32 ms, faster than 93.78% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.8 MB, less than 28.00% of Python3 online submissions for Clone Graph.

