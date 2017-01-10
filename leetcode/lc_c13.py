class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def findsum(nums,v):
            for i in xrange(len(nums)):
                for j in xrange(i,len(nums)):
                    if sum(nums[i:j+1])==v:
                        nums = nums[:i]+nums[j+1:] if i>0 else nums[j+1:]
                        return True,nums
            return False,nums

        def dfs(nums,p,n):
            if n==0:
                return True
            if len(nums)<n:
                return False
            v = p-nums.pop()
            if v==0:
                return dfs(nums,p,n-1)
            found,nums = findsum(nums,v)
            return dfs(nums,p,n-1) if found else False
            
        nums.sort()
        N = sum(nums)
        if len(nums)<4 or N%4 >0 or nums[-1]>N/4:
            return False
        return dfs(nums,N/4,4)
        
from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.makesquare([10,6,5,5,5,3,3,3,2,2,2,2]))
        self.assertTrue(self.solution.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
        self.assertTrue(self.solution.makesquare([1,1,2,2,2]))
        self.assertFalse(self.solution.makesquare([3,3,3,3,4]))

    def tearDown(self):
        self.solution = None

def debug_test():
    solution = Solution()
    solution.makesquare([10,6,5,5,5,3,3,3,2,2,2,2])

if __name__ == '__main__':
    main()
