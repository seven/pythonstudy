class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        def is_after(b,a):
            if ord(a)==ord('z'):
                return ord(b)==ord('a')
            else:
                return ord(a)+1==ord(b)

        f=1
        m={p[0]:1}
        for i in xrange(1,len(p)):
            f=1+f if is_after(p[i],p[i-1]) else 1
            if f> m.get(p[i],0):
                m[p[i]]=f
        return sum(m.values())

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.findSubstringInWraproundString("a"),1)
        self.assertEqual(self.solution.findSubstringInWraproundString("cac"),2)
        self.assertEqual(self.solution.findSubstringInWraproundString("zab"),6)

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
