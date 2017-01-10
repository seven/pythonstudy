class Solution(object):
    #solution 1: dfs search on sorted nums
    def dfs(self,N, nums,index, target,path,res):
        if len(path) == N:
            if target ==0:
                res.append(path[:])
        else:
            for i in xrange(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                else:
                    self.dfs(N,nums,i+1,target-nums[i],path+[nums[i]],res)
            

    #solution 2: reduce to twosum problem solved by two pointers
    def NSum(self,N, nums,index, target,path,res):
        def twoSum(nums,index,t,path,res):
            c,d = index,len(nums)-1
            while c<d:
                if c>index and nums[c] == nums[c-1]:
                    c+=1
                    continue
                if d<N-1 and nums[d] == nums[d+1]:
                    d-=1
                    continue

                if nums[c]+nums[d] == t:
                    res.append(path+ [nums[c],nums[d]])
                    c+=1
                    d-=1
                elif nums[c]+nums[d] < t:
                    c+=1
                else:
                    d-=1


        nums.sort()
        if N>2:
            for a in xrange(index,len(nums)-N+1):
                if a>index and nums[a] == nums[a-1]:
                    continue
                self.NSum(N-1,nums,a+1,target-nums[a],path+[nums[a]],res)#reduce by N-1
        else:
            twoSum(nums,index,target,path,res)

        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        #self.NSum(4,nums,0,target,[],res)
        self.dfs(4,nums,0,target,[],res)
        return res


        
from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        nums = [0,0,0,0]
        res = self.solution.fourSum(nums,0)
        exp=[[0,0,0,0]]
        self.assertListEqual(sorted(res),sorted(exp))

        nums = [1,-2,-5,-4,-3,3,3,5]
        res = self.solution.fourSum(nums,-11)
        exp= [[-5,-4,-3,1]]
        self.assertListEqual(sorted(res),sorted(exp))

        nums = [-3,-2,-1,0,0,1,2,3]
        res = self.solution.fourSum(nums,0)
        exp= [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertListEqual(sorted(res),sorted(exp))


    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
