class Solution(object):
    def play(self,a,b):
        if a>=b:
            return 0
        if a+1==b:
            return a
        if a+2==b:
            return (a+b)/2
        k=str((a,b))
        if k in self.m:
            return self.m[k]
        t= 1<<32
        for x in xrange(a,b+1):
            t = min(t,x+max(self.play(a,x-1),self.play(x+1,b)))
        self.m[k]=t
        return t

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=[[0]*(n+1) for _ in xrange(n+1)]
        for i in xrange(n,0,-1):
            for j in xrange(i+1,n+1):
                f[i][j]=min(x+max(f[i][x-1],f[x+1][j]) for x in xrange(i,j))
        return f[1][n]
            
        
        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.getMoneyAmount(1)==0)
        self.assertTrue(self.solution.getMoneyAmount(2)==1)
        self.assertTrue(self.solution.getMoneyAmount(7)==10)

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
