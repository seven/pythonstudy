class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        c1= Counter((a+b for a in A for b in B))
        c2= Counter((c+d for c in C for d in D))
        return sum((c1[k]*c2[-k] for k in c1 if -k in c2))

    def fourSum(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype:  List[List[int]]
        """
        def sumdict(A,B):
            m={}
            for a in A:
                for b in B:
                    m.setdefault(a+b,[]).append([a,b])
            return m

        m1,m2=sumdict(A,B),sumdict(C,D)
        res=[]
        for k in m1:
            if -k in m2:
                from itertools import product
                res+=[x1+x2 for x1 in m1[k] for x2 in m2[-k]]
        return res


from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]
        self.assertEqual(self.solution.fourSumCount(A,B,C,D),2)
        print(self.solution.fourSum(A,B,C,D))

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
