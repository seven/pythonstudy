class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n=len(str)
        for k in xrange(2,n+1):
            if n%k ==0:
                s=n/k
                t=True
                for i in xrange(1,k):
                    if str[s*(i-1):s*i] != str[s*i:s*(i+1)]:
                        t=False
                if t:
                    return True
        return False 


from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.repeatedSubstringPattern("aa"))
        self.assertTrue(self.solution.repeatedSubstringPattern("aaa"))
        self.assertTrue(self.solution.repeatedSubstringPattern("abcabcabc"))
        self.assertTrue(self.solution.repeatedSubstringPattern("abcabcabcabc"))

        self.assertFalse(self.solution.repeatedSubstringPattern("a"))
        self.assertFalse(self.solution.repeatedSubstringPattern("abc"))

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
