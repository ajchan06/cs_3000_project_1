#Aahana Surya, Jun 1, 2026
#CS3000 Algorithms, Project #1
#Problem #2 Code File: Find All Nodes Distance K in Binary Tree

class Solution(object):   
    def distanceK(self, root, target, k):
        parent = {} 
        def buildParent(node, par): #this stores all parent nodes together
            if not node:
               return
            parent[node] = par 
            buildParent(node.left, node)
            buildParent(node.right, node)
        buildParent(root, None)
        answer = []
        visited = set()
        def dfs(node, distance):
            if not node or node in visited:
               return
            visited.add(node)
            if distance == k:
               answer.append(node.val)
               return
            dfs(node.left, distance + 1)
            dfs(node.right, distance + 1)
            dfs(parent[node], distance + 1)
        dfs(target, 0)
        return answer
