class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nabo(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1,1):
                    y = (x+d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        dead = set(deadends)
        q = [('0000',0)]
        seen ={'0000'}
        while q:
            node, depth = q.pop(0)
            if node == target:
                return depth
            if node in dead:
                continue
            for n in nabo(node):
                if n not in seen:
                    seen.add(n)
                    q.append((n,depth+1))
        return -1
        
