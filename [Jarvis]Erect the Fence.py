class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def orient(p,q,r):
            return (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
        def inBetween(p,i,q):
            a= p[0] <= i[0]<=q[0] or q[0]<=i[0]<=p[0]
            b= p[1]<=i[1]<=q[1] or q[1]<=i[1]<=p[1]
            return a and b
        if len(points)<4:
            return points
        points.sort()
        m = set()
        p,q=0,1
        hull=[]
        while q!=0:
            hull.append(points[p])
            m.add(p)
            q = (p+1) %len(points)
            for r in range(len(points)):
              # 发生右拐,r比q更近, update q as r, until find the furthest point as q
                if orient(points[p],points[r], points[q]) <0:
                    q=r 
            for r in range(len(points)):
              #r is in the same line with p and q, and in between p and q, add r to the result set
                if r!=q and r!=p and orient(points[p],points[q],points[r]) ==0 and inBetween(points[p],points[r],points[q]) and r not in m:
                    hull.append(points[r])
                    #register r as seen points
                    m.add(r)
            #come from p to q
            p=q
        return hull
