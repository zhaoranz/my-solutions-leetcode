class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
      #get the directed children of each node
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count =[1]*n #count number of children of each node + 1, the node itself
        ans =[0]*n #record answers
        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child !=parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child !=parent:
                  # count(parent) = N - count(x)
                  #ans[child]=ans[parent] + count[parent] - count[child]= ans[parent]+(n-count[child])-count[child]
                    ans[child]=ans[node] - count[child]+n-count[child]
                    dfs2(child, node)
        # 1.求出 ans[0] 并统计出每个子树的节点数目
        dfs()
        # 2.根据公式和 ans[0] 计算其余结果
        dfs2()
        return ans
