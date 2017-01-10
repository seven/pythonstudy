class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums)/2]
        return sum( abs(median-x) for x in nums)
        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.minMoves2([1,2,3]),2)
        self.assertEqual(self.solution.minMoves2([1,0,0,8,6]),14)
        self.assertEqual(self.solution.minMoves2([-1,-2,1,2,3]),8)

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
