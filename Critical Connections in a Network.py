class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        res =[]
        dfn =[-1] * n
        low =[-1] * n
        
        def tarjan(node, parent, depth):
            dfn[node] = depth
            low[node] = depth
            for nex in graph[node]:
                if nex == parent:
                    continue
                if dfn[nex] ==-1:
                    tarjan(nex, node, depth+1)
                    if dfn[node] < low[nex]:
                        res.append([node,nex])
                low[node] = min(low[node], low[nex])
        tarjan(0,-1,0)
        return res
