class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        res =set()
        l1, val =[],1
        if x!=1:
            upper = math.floor(math.log(bound-1, x))
            if x**upper <= bound -1:
                upper +=1
            for i in range(upper+1):
                l1.append(val)
                val *= x
        else:
            l1.append(1)
        l2, val =[],1
        if y !=1:
            upper = math.floor(math.log(bound-1, y))
            if y**upper <= bound -1:
                upper +=1
            for i in range(upper+1):
                l2.append(val)
                val *= y
        else:
            l2.append(1)
        end = len(l1)-1
            
        for i in l2:
            while end >= 0 and l1[end] + i > bound:
                end -=1
            for j in range(end+1):
                res.add(l1[j]+i)
            
            
        return list(res)
        
