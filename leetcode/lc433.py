class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
        """
        a=[start]
        res=0
        def change(e):
            dic=['A','C','G','T']
            for i in xrange(8):
                for j in xrange(4):
                    if e[i]!=dic[j]:
                        yield e[:i]+dic[j]+e[i+1:]
            
        while a:
            level=[]
            res+=1
            if res>8:
                return -1

            for e in a:
                for x in change(e):
                    if x in bank:
                        if x==end:
                            return res
                        level.append(x)
            a=level
        return -1
        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        start="AAAAACCC"
        end="AACCCCCC"
        bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        self.assertEqual(self.solution.minMutation(start,end,bank),3)
        self.assertEqual(self.solution.minMutation("AACCGGTT","AACCGGTA",[]),-1)

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
