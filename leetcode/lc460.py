class LFUCache(object):
    from heapq import *

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n=capacity
        self.keys=[]
        self.m={}
        
    def _update(self, key):
        for i,t in enumerate(self.keys):
            if t[1]==key:
                self.keys[i]=t[0]+1,key
        heapify(self.keys)

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.m:
            return -1

        self._update(key)
        return self.m[key]

    def _pop(self):
        c,k= heappop(self.keys)
        self.m.pop(k) 

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.m:
            self._update(key)
        else:
            heappush(self.keys,(1,key))
        self.m[key]=value
        if len(self.keys) >self.n:
            self._pop()
        
from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def test_solution(self):
        cache = LFUCache( 2 )
        cache.set(1, 1)
        cache.set(2, 2)
        self.assertEqual(1, cache.get(1))       # returns 1
        cache.set(3, 3)    # evicts key 2
        self.assertEqual(-1, cache.get(2))       # returns -1 (not found)
        self.assertEqual(3, cache.get(3))       # returns 3.
        cache.set(4, 4)    # evicts key 1.
        self.assertEqual(-1,cache.get(1))       # returns -1 (not found)


if __name__ == '__main__':
    main()
