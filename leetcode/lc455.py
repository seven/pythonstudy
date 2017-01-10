# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def add(self, l1, l2,dis):
        if not l1:
            return 0

        t = l1.val
        if dis==0:
            t+=l2.val + self.add(l1.next,l2.next,0)
        else:
            t+=self.add(l1.next,l2,dis-1)
        l1.val = t%10
        return 1 if t > 9 else 0
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def size(node):
            n=0
            while node:
                n+=1
                node = node.next
            return n
        n1=size(l1)
        n2=size(l2)
        if n1<n2:
            l1,l2=l2,l1
            n1,n2=n2,n1

        if self.add(l1,l2,n1-n2)>0:
            head = ListNode(1)
            head.next = l1
            return head
        else:
            return l1
        
            
        

from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        pass

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    main()
