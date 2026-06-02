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
