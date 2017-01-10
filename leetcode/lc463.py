class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        for i,j in grid:
            if grid[i][j]:
                res+=4
                if i>0 and grid[i-1][j]:
                    res-=2
                if j>0 and grid[i][j-1]:
                    res-=2

        """
        res =0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j]:
                    res+=4
                    if i>0 and grid[i-1][j]:
                        res-=2
                    if j>0 and grid[i][j-1]:
                        res-=2
        return res
                


from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        grid= [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertTrue(self.solution.islandPerimeter(grid)==16)

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
