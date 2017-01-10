class Solution(object):
    def win(self, a,t):
        key = str(a)
        if a and a[-1]>=t:
            return True
        if key in self.m:
            return self.m[key]

        for i,v in enumerate(a):
            if not self.win(a[:i]+a[i+1:],t-v):
                self.m[key] = True
                return True
        self.m[key] = False
        return False
        
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        a = range(1,maxChoosableInteger+1)
        t = desiredTotal
        if maxChoosableInteger*(1+maxChoosableInteger)<t:
            return False
        self.m={}
        return self.win(a,t)

        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.canIWin(10,10))
        self.assertFalse(self.solution.canIWin(10,11))
        self.assertTrue(self.solution.canIWin(10,12))
        self.assertFalse(self.solution.canIWin(18,188))
        self.assertFalse(self.solution.canIWin(16,225))

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
