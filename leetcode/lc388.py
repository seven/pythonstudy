class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res=0
        path=[0]*(1+input.count("\n"))
        it =(x.split("\t")  for x in input.splitlines())
        for r in it:
            tabs = len(r)-1
            name = r[-1]
            isFile=name.count(".")>0
            if isFile:
                res = max(res, tabs+ len(name) + sum(path[:tabs]))
            else:
                path[tabs]=len(name)
        return res

        
        
from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        self.assertEqual(self.solution.lengthLongestPath(input),32)
        self.assertEqual(self.solution.lengthLongestPath("a"),0)


    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
