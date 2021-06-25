class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents, ranks = {},{}
        def find_parent(n, parents):
            while parents[n] !=n:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n
        for edge in edges:
            u,v = edge[0], edge[1]
            if u not in parents:
                parents[u]=u
                ranks[u]=1
            if v not in parents:
                parents[v] =v
                ranks[v] = 1
            pu = find_parent(u, parents)
            pv = find_parent(v, parents)
            if pu == pv:
                return edge
            if ranks[pu] > ranks[pv]:
                parents[pu] = pv
                ranks[pv] += ranks[pu]
            else:
                parents[pv]=pu
                ranks[pu] += ranks[pv]
