class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        l1,l2=len(nums1), len(nums2)
        intersection=[]
        i,j=0,0
        while i< l1 and j<l2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                intersection.append(nums1[i])
                i+=1
                j+=1
        return intersection
      
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=collections.Counter(nums1)
        n2=collections.Counter(nums2)
        n=n1& n2
        return n.elements()
        
