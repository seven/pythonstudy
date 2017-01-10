def partition(a):
    if len(a)<2:
        return 0
    p=a[-1]
    i,j=0,len(a)-2
    while True and i<j:
        while i<j and a[i]>=p:i+=1
        while i<j and p>a[j]: j-=1
        if i<j: a[i],a[j]=a[j],a[i]
        else: break
    if a[i]< p:
        a[i],a[-1] = a[-1],a[i]
        return i
    else:
        return len(a)-1
    
def findKth(a,k):
    if not a:
        return 0
        
    #find kth in a[:]
    i = partition(a)
    #a[0:i-1] >=a[i]> a[i+1:]
    if i+1 == k:
        return a[i]
    elif i+1<k:
        return findKth(a[i+1:],k-i-1)
    else:
        return findKth(a[:i],k)
        
 
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return findKth(nums,k)
        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(findKth([1,2],1),2)
        self.assertEqual(findKth([2,1],1),2)
        self.assertEqual(findKth([2,1,3],1),3)
        self.assertEqual(findKth([2,1,3],2),2)
        self.assertEqual(findKth( [5,2,4,1,3,6,0], 2),5)
    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
